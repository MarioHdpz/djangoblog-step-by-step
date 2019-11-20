""" Blog serializers for API """
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """ All post data serializer """

    class Meta():
        model = Post
        fields = "__all__"
