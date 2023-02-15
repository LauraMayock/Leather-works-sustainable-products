from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, View
from .models import Post
from django.utils.text import slugify
from .forms import ContactForm


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

