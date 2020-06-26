from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils import timezone

# Create your models here.

def upload_profile_picture(instance, filename):
	return "post_pics/{timezone}/{account_to}/{filename}".format(account_to=User, filename=filename, timezone=timezone.now())

class Blog(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	meme_image = models.ImageField(blank=False, null = False, upload_to=upload_profile_picture)

	def __str__(self):
		return self.title


