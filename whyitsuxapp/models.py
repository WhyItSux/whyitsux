from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models

from whyitsuxapp.managers import TopicManager

class Category(models.Model):
	name = models.CharField(max_length=128)
	sites = models.ManyToManyField(Site)

	parent = models.ForeignKey('self', null=True, blank=True)

	objects = models.Manager()
	on_site = CurrentSiteManager()

	def __str__(self):
		return self.name

class Topic(models.Model):
	name = models.CharField(max_length=128)
	category = models.ManyToManyField(Category)

	objects = models.Manager()
	on_site = TopicManager()

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Comment(models.Model):
	content = models.TextField()
	parent = models.ForeignKey('self')

	def __str__(self):
		return self.content

class Post(Comment):
	title = models.CharField(max_length=128)

	topic = models.ForeignKey(Topic)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title
