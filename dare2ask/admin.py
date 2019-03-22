from django.contrib import admin
from dare2ask.models import Lecture, Question, UserProfile

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Question)
admin.site.register(UserProfile)
