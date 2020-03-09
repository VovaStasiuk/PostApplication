from rest_framework import serializers
from ..models import Post
from apps.likes import utils, models


class PostSerializer(serializers.ModelSerializer):

    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'is_liked', 'total_likes',)

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return utils.is_like(obj, user)
