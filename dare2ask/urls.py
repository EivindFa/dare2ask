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
	url(r'^search/(?P<search_slug>[\w\-]+)$',
		views.search, name = 'search'),
	url(r'^delete/(?P<lecture_name_slug>[\w\-]+)/confirm$',
		views.delete_conf, name = 'delete_conf'),
	url(r'^delete/(?P<lecture_name_slug>[\w\-]+)/$',
		views.delete, name = 'delete'),
	url(r'^register_profile/$',
		views.register_profile, name='register_profile'),
	url(r'^profile/(?P<username>[\w\-]+)/$',
		views.profile, name='profile'),
	url(r'^like/$', views.like_question, name='like_question'), # temporary like id for AJAX - EF
]
