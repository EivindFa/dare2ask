from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=128, unique = True)
    join_ID = models.IntegerField(default = -1)
    course_num = models.CharField(max_length=128, default = -1)

    slug = models.SlugField(unique = True) # (blank = True)
    max_length = 128

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Lecture, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Question(models.Model):
    lecture = models.ForeignKey(Lecture)    # Holds parent Lecture, one-to-many relationship
    text = models.CharField(max_length=128)
    upvotes = models.IntegerField(default = 0)
    answered = models.BooleanField(default = False)

    def __str__(self):
        return self.text

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful!
	def __str__(self):
		return self.user.username
