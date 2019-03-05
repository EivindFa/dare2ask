from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from dare2ask import views

app_name = 'dare2ask'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^lecture/$', views.lecture, name='lecture'),
]
