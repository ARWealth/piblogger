"""Views for pibloggers."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Title, BlogPost
from .forms import TitleForm, BlogPostForm


def index(request):
	"""The home page for PiBloggers."""
	titles = Title.objects.order_by('date_entered')
	context = {'titles': titles}
	return render(request, 'pibloggers/index.html', context)


def title(request, title_id):
	""" Show blog entries for a particular topic."""
	title = Title.objects.get(id=title_id)
	blog_posts = title.blogpost_set.order_by('-date_entered')
	context = {'title': title, 'blog_posts': blog_posts}
	return render(request, 'pibloggers/title.html', context)


@login_required
def new_title(request):
	""" Add a new title for a blog post."""
	if request.method != 'POST':
		# If no data is submitted, create a blank form
		form = TitleForm()
	else:
		# POST data submitted; process data
		form = TitleForm(data=request.POST)
		if form.is_valid():
			new_title = form.save(commit=False)
			new_title.blogger = request.user
			new_title.save()
			return redirect('pibloggers:index')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'pibloggers/new_title.html', context)


@login_required
def new_blogpost(request, title_id):
	""" Write an entry for a blogpost."""
	title = Title.objects.get(id=title_id)

	# Ensure the blogger is writing his own post before processing the form
	if title.blogger != request.user:
		raise Http404

	if request.method != 'POST':
		# Create a blank form if the user sends a GET request.
		form = BlogPostForm()
	else:
		# POST data submitted; process data
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			# Create a new blogpost and assign it to new_blogpost without saving
			# it to the database yet
			new_blogpost = form.save(commit=False)
			new_blogpost.title = title
			new_blogpost.save()
			return redirect('pibloggers:title', title_id=title_id)

	# Display a blank or invalid form
	context = {'title': title, 'form': form}
	return render(request, 'pibloggers/new_blogpost.html', context)


@login_required
def edit_blogpost(request, blogpost_id):
	""" Edit an existing blog post. """
	blogpost = BlogPost.objects.get(id=blogpost_id)
	title = blogpost.title

	# Ensure the blogger is editing his own post before processing the form
	if title.blogger != request.user:
		raise Http404

	if request.method != 'POST':
		# If no edits has been done, display the current post
		form = BlogPostForm(instance=blogpost)
	else:
		# POST data submitted; process data
		form = BlogPostForm(instance=blogpost, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('pibloggers:title', title_id=title.id)

	context = {'blogpost': blogpost, 'title': title, 'form': form}
	return render(request, 'pibloggers/edit_blogpost.html', context)






