from django.conf.urls import url
from dare2ask import views

app_name = 'dare2ask'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
]