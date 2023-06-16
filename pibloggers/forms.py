"""Forms for users to make entries to PiBlogger app."""
from django import forms

from .models import Title, BlogPost


class TitleForm(forms.ModelForm):
	class Meta:
		model = Title
		fields = ['title']
		labels = {'title': ''}

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}

