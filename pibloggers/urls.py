"""Defines URL patterns for app pibloggers."""

from django.urls import path

from . import views

app_name = 'pibloggers'
urlpatterns = [
	# Home Page for pibloggers
	path('', views.index, name='index'),

	# Page to view a blog post
	path('title/<int:title_id>/', views.title, name='title'),

	# Page to add a new title.
	path('new_title/', views.new_title, name='new_title'),

	# Page to write a new blog post.
	path('new_blogpost/<int:title_id>/', views.new_blogpost, name='new_blogpost'),

	# Page to edit a blog post
	path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),

]