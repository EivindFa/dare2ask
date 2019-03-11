from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from dare2ask import views

app_name = 'dare2ask'
urlpatterns = [
	url(r'^$',
		views.index, name='index'),
	url(r'^about/$',
		views.about, name='about'),
	url(r'^lecture/$',
		views.lecture, name='lecture'),
	url(r'^lecture/(?P<lecture_name_slug>[\w\-]+)/$',
		views.in_lecture, name='in_lecture'),
	url(r'^register_profile/$', 
		views.register_profile, name='register_profile'),
	url(r'^profile/(?P<username>[\w\-]+)/$', 
		views.profile, name='profile'),
]
