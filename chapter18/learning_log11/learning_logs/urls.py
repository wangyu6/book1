"""定义learning_log的URL模式"""

from django.urls import include, path,re_path
from . import views
app_name = '[learning_logs]'
urlpatterns = [
    #主页
    re_path(r'', views.index, name= 'index.html'),
    re_path(r'^topics/',views.topics,name='topics'),
]
    
