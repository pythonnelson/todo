from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

from . views import *

app_name = 'todo'

urlpatterns = [
	path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),
	path('logout/', logoutuser, name='logout'),

	path('', listTask, name="task_list"),
	path('update_task/<str:pk>/', updateTask, name="update_task"),
	path('delete_task/<str:pk>/', deleteTask, name="delete_task"),
	path('add_category/', addCategory, name="add_category"),

	path('date/', displayDate, name='date'),

	########################## DOWNLOAD AND UPLOAD URLS #####################

	url(r'^download/(?P<path>>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]