from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class TaskForm(forms.ModelForm):
	# category_title=forms.CharField()
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)

	class Meta:
		model = task
		fields = ['category', 'level_of_priority', 'title', 'due']


class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = task
		fields = ['category', 'level_of_priority', 'title', 'due', 'complete']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


	# def cleaned_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	email_req = "govmail.gov.sl"
	# 	if not email_req in email:
	# 		raise forms.ValidationError("Email not recognized")
	# 	raise email


class AddCategoryForm(forms.ModelForm):
	category = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add New Category'}), label=False)

	class Meta:
		model = Category
		fields = ['category',]