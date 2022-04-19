from django import views
from django.urls import path
from . import views

urlpatterns = [ path('/polls',views.index,name='index'),]