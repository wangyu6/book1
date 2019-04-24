from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import Topic


def index(request):
	"""学习笔记的主页"""
	# return HttpResponse('hello')
	return render(request, 'learning_logs/index.html')

def topics(request):
	"""显示所有主题"""
	topics = Topic.object.oder_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/base.html',context)