from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
		path ('converter/',views.index,name='index'),
		]