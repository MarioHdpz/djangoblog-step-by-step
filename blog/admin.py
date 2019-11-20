""" Add blog models to admin """
from django.contrib import admin

from blog.models import Post, Author, Tag

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
