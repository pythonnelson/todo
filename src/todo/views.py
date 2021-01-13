from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *
from . reminder import reminder

from plyer import notification
import datetime



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, "Account created for " + user)
				return redirect("todo:login")
		context = {'form':form,}
		return render(request, "accounts/register.html", context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, "Mismatched credentials, please try again")
		context = {}
		return render(request, "accounts/login.html", context)


def logoutuser(request):
	logout(request)
	return redirect('todo:login')


@login_required(login_url='todo:login')
def listTask(request):

	queryset = task.objects.order_by('-level_of_priority', 'due', 'complete') #'complete',

	form = TaskForm()

	if request.method =='POST':

		form = TaskForm(request.POST)

		if form.is_valid():

			form.save()

			messages.success(request, 'Task Successfully Saved')

	paginator = Paginator(queryset, per_page=3)
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)


	context = {

		'tasks':page_obj.object_list, #queryset,

		'form':form,

		'reminder':reminder,

		'file':FilesAdmin.objects.all(),

		'paginator': paginator,

		'page_number': int(page_number),

	}

	return render(request, 'todo/list_task.html', context)

# def taskreminder(request):
# 	queryset = task.objects.get(id=pk)
# 	start_date = datetime.datetime.now()
# 	end_date = datetime.datetime()
# 	if start_date == end_date - str(30):
# 		reminder(task.title)
# 	else:
# 		pass


@login_required(login_url='todo:login')
def updateTask(request, pk):
	queryset = task.objects.get(id=pk)
	form = UpdateForm(instance=queryset)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Task Successfully Updated')
			return redirect('/')

	context = {
		'form':form
		}

	return render(request, 'todo/update_task.html', context)


@login_required(login_url='todo:login')
def deleteTask(request, pk):
	queryset = task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Task Successfully Deleted')
		return redirect('/')

	context = {
		'item':queryset
		}
	return render(request, 'todo/delete_task.html', context)


def download(request, path):

	file_path = os.path.join(settings.MEDIA_ROOT, path)

	if os.path.exists(file_path):
		with open(file_path, 'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminUpload")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response
	raise Http404



def addCategory(request):

	form = AddCategoryForm()

	if request.method == 'POST':

		form = AddCategoryForm(request.POST)

		if form.is_valid():

			form.save()

			return redirect('/')

	context = {

		'title': 'Add New Category',
		'form': form,

	}

	return render(request, 'todo/category.html', context)

def displayDate(request):
	display_date = datetime.date.today()
	return HttpResponse(
		display_date
	)
