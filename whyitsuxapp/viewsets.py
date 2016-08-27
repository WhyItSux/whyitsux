from django.contrib.sites.shortcuts import get_current_site
from rest_framework import viewsets

from whyitsuxapp import models, serializers

class Categories(viewsets.ReadOnlyModelViewSet):
	queryset = models.Category.on_site.all()
	serializer_class = serializers.CategorySerializer

class Topics(viewsets.ReadOnlyModelViewSet):
	queryset = models.Topic.on_site.all()
	serializer_class = serializers.TopicSerializer

class Comments(viewsets.ModelViewSet):
	queryset = models.Comment.objects.all()
	serializer_class = serializers.CommentSerializer

class Posts(viewsets.ModelViewSet):
	queryset = models.Post.objects.all()
	serializer_class = serializers.PostSerializer

class Tags(viewsets.ReadOnlyModelViewSet):
	queryset = models.Tag.objects.all()
	serializer_class = serializers.TagSerializer
