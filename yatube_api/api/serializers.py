from django.shortcuts import get_object_or_404
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    def validate_following(self, value):
        following = get_object_or_404(User, username=value)
        if Follow.objects.filter(
                user=self.context.get('request').user, following=following
        ).exists():
            raise serializers.ValidationError(
                f'Подписка на - {following.username} уже подтверждена'
            )
        if self.context.get('request').user == following:
            raise serializers.ValidationError(
                'Нельзя подписываться на себя'
            )
        return value

    class Meta:
        fields = '__all__'
        model = Follow
