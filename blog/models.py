from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=30)
	
	class Meta:
		verbose_name_plural = "categories"
	
	def __str__(self):
		return self.name
	
class Post(models.Model):
	title = models.CharField(max_length=255)
	#author = models.ForeignKey(User, on_delete = models.CASCADE) #usuwa posty gdy usuwam uzytkownika
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField("Category", related_name="posts")
	
	def __str__(self):
		return self.title #+ ' | ' f"(self.author) on '(self.Post)'"
	
class Comment(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey("Post",on_delete=models.CASCADE)
	
	def __str__(self):
		return f"(self.author) on '(self.post)'"


# Create your models here.
