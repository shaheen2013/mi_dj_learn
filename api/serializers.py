from rest_framework import serializers
from posts.models import Post


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=254)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    image = serializers.FileField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('linenos', instance.image)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
