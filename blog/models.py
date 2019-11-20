""" Blog models """
from django.db import models

class Author(models.Model):
    """ Post author """
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40, blank=False)
    slug = models.SlugField(max_length=60, blank=True, default='')

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

class Tag(models.Model):
    """ Post tags """
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    """ Post """
    content = models.TextField(blank=False)
    header = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=60, blank=True)
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
