import datetime
from django.db import models


class Category(models.Model):
	category = models.CharField(max_length=200, default="Select Category")

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category


LEVEL_OF_PRIORITY = (
		("Low", "Low"),
		("Medium", "Medium"),
		("High", "High"),
		("Very High", "Very High"),
	)


class task(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default="Select Category")
	title = models.CharField(max_length=200)
	level_of_priority = models.CharField("Level of Priority", max_length=100, choices=LEVEL_OF_PRIORITY, default='')
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
	start_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,null=True)
	end_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,null=True)

	def __str__(self):
		return self.title


class FilesAdmin(models.Model):
	adminUpload = models.FileField(upload_to='media')
	title = models.CharField(max_length=100)


	def __str__(self):
		return self.title
