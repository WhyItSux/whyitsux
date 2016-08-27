from django.contrib.sites.models import Site
from django.db import models

class TopicManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(category__sites=Site.objects.get_current())
