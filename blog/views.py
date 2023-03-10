from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, CreateView, View
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from .forms import ContactForm, BlogPost, CreatePost
from django.contrib import messages


class PostList(ListView):
    """
    Takes the Post Model and makes sure they are
    approved and displayes them on the home page
    """
    model = Post
    template_name = "blog.html"
    paginate_by = 6


class PostDetail(View):
    """
    Gets full post
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_details.html",
            {
                "post": post,
            },
        )


@login_required
def update_post(request, post_id):
    """
    Users can update book reviews that they have
    created using a form
    """
    post = Post.objects.get(pk=post_id)
    form = BlogPost(request.POST or None, instance=post)
    if post.author != request.user:
        return redirect('This is not your Post')
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')

    return render(request,
                  'update_post.html',
                  {'update-post': post, 'form': form})


@login_required
def delete_post(request, post_id):
    """
    Users can delete post
    """
    pst = Post.objects.get(pk=post_id)
    context = {'pst': pst}

    if request.method == 'POST':
        pst.delete()
        messages.success(request,
                         ('You have deleted this review sucessfully.'))
        return redirect('blog')

    return render(request, 'delete.html', context)


@login_required
class AddPost(CreateView):
    """
    Ensures that person is logged in to create
    a blog post
    """
    template_name = 'add_post.html'
    model = Post
    form_class = CreatePost

    def form_valid(self, form):
        """_summary_
        validates the form and adds a success message
        to the template once a Post is successfully added
        Sets the automatic slug for the object created
        from the user input on the title
        field
        """
        form.instance.author = self.request.user
        messages.success(
            self.request,
            'Your blog post has now been posted')
        form.slug = slugify(form.instance.title)
        return super().form_valid(form)


def contact(request):
    """
    Submits contact us form to the admin dashboard.

    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted = True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html',
                  {'form': form, 'submitted': submitted})


class Faqs(CreateView):
    """
    Displays Frequently asked questions page.
    """
    template_name = 'faqs.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def sustainable_leather(View):
    model = Post
    queryset = Post.objects.filter(title="What is Sustainable Leather?")
    return HttpResponseRedirect('/blog/what-is-sustainable-leather/')


def meet_the_tanner(View):
    model = Post
    queryset = Post.objects.filter(title="Meet the chief Tanner")
    return HttpResponseRedirect('/blog/meet-the-chief-tanner/')


def certs(View):
    model = Post
    queryset = Post.objects.filter(
        title="We are a Certified Sustainable leather Manufacturer.")
    return HttpResponseRedirect('/blog/we-are-a-certified/')


def custom(View):
    model = Post
    queryset = Post.objects.filter(title="Bespoke Made to Order")
    return HttpResponseRedirect('/blog/bespoke-made-to-order/')
