from rest_framework import serializers

from .models import Post
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'published_at']
        read_only_fields = ('published_at',)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
