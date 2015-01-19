from django.db import models

import datetime

# Create your models here.

#class List(models.Model):
#	title = models.CharField(max_length= 250, unique= True)
	
#	def __str__(self):
#		return self.title

#	class Meta:
#		ordering= ['title']

#	class Admin:
#		pass


PRIORITY_CHOICES = (
					(1,'VERY LOW'),
					(2, 'LOW'),
					(3, 'NORMAL'),
					(4, 'HIGH'),
					(5, 'VERY HIGH'),
					)

TASK_STATUS = 	(
				(1, 'ToDo'),
				(2, 'Doing'),
				(3, 'Done'),
				)


class Item(models.Model):
	title= models.CharField(max_length= 250)
	description= models.CharField(max_length= 500, default= 'No description')
	due_date= models.DateTimeField()
	priority= models.IntegerField(choices= PRIORITY_CHOICES, default= 2)
	status= models.IntegerField(choices= TASK_STATUS)
	#todo_list= models.ForeignKey(List)

	def __str__(self):
		return self.title

	class Meta:
		ordering= ['priority', 'title']

	class Admin:

		pass
		
