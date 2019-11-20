""" Blog views """
from django.views.generic import ListView

from .models import Post

class AllPosts(ListView):
    """ Render all posts """
    template_name = "blog.html"
    context_object_name = "posts"
    model = Post
