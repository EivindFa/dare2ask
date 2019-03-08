from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Lecture(models.Model):
    name = models.CharField(max_length=128, unique = True)
    join_ID = models.IntegerField(default = -1)
    print('5')
    print(join_ID)
    #course_num = models.CharField(max_length=128, default = -1)

    slug = models.SlugField(unique = True) # (blank = True)
    print('6')
    print(slug)
    max_length = 128

    def save(self, *args, **kwargs):
        print('FLAG 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        self.slug = slugify(self.title)
        super(Lecture, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Question(models.Model):
    lecture = models.ForeignKey(Lecture)    # Holds parent Lecture,
                                            # one-to-many relationship
    text = models.CharField(max_length=128) # Actual question
    upvotes = models.IntegerField(default = 0)
    answered = models.BooleanField(default = False)

    def __str__(self):
        return self.text

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User) # Name of user
	email = models.EmailField(max_length = 254, unique = True)
	tutor = models.BooleanField(default = False)

	# The additional attributes we wish to include
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful!
	def __str__(self):
		return self.user.username
