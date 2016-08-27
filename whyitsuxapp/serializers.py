from django.contrib.sites.models import Site
from rest_framework import serializers

from whyitsuxapp import models

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Category
		fields = ('name',)

class TopicSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Topic

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Comment

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Post

class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Tag
