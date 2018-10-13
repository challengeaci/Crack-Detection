from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^DeepAgri/$',views.DeepAgri.as_view(),name='DeepAgri'),
    url(r'^home/$', views.home,name='index'),
]
