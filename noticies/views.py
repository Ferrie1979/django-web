from django.shortcuts import render
from .models import post

# Create your views here.

def post_list(request):
	noticia = post.objects.order_by('creacio_post')
	return render(request,'post_list.html',{'nots':noticia})