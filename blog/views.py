""" Blog views """
from django.views.generic import ListView, DetailView

from .models import Post

class AllPosts(ListView):
    """ Render all posts """
    template_name = "blog.html"
    context_object_name = "posts"
    model = Post

class PostDetail(DetailView):
    """ Render a specific post """
    template_name = "detail.html"
    context_object_name = "post"
    model = Post

class PostsByAuthor(AllPosts):
    """ Render a specific post """
    def get_queryset(self):
        return Post.objects.filter(author__slug=self.kwargs['slug'])
