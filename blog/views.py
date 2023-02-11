from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    """
    Takes the Post Model and makes sure they are
    approved and displayes them on the home page
    """
    model = Post
    template_name = "blog.html"
    paginate_by = 6



