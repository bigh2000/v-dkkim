from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True, null=True)
	posted_at = models.DateTimeField(auto_now_add=True)
	edited_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title