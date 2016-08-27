from django.db import models

class Category(models.Model):
	pass

class Topic(models.Model):
	pass

class Comment(models.Model):
	pass

class Post(Comment):
	pass

class Tag(models.Model):
	pass
