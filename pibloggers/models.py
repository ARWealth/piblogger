from django.db import models
from django.contrib.auth.models import User


class Title(models.Model):
	"""Model the title of a blog post."""
	title = models.CharField(max_length=255)
	date_entered = models.DateTimeField(auto_now_add=True)
	blogger = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		"""Return a string representation of the Title model."""
		return self.title


class BlogPost(models.Model):
	"""Model a blog entry."""
	title = models.ForeignKey(Title, on_delete=models.CASCADE)
	text = models.TextField()
	date_entered = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'blog_posts'


	def __str__(self):
		"""Return a string representation of the BlogPost model."""
		return self.text
