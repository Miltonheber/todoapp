from django.db import models

# Create your models here.

class task(models.Model):
	tarefa = models.CharField('Task',max_length=100)
	
	def __str__(self):
		return self.tarefa
		

