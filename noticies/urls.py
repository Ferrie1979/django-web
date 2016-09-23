# urls de noticies
from django.conf.urls import include,url
from .import views

urlpatterns = [
	url(r'^$',views.post_list),
	url(r'^noticies/$',views.post_list),
]