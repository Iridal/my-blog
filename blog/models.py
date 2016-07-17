from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date  = models.TextField(default=timezone.now) #usa el atributo now
	published_date = models.DateTimeField(blank=True, null=True) #blank permite valores blancos en formularios, null es a nivel de base de datos

	def publish(self):
		self.published_date = timezone.now() #usa la función now
		self.save()

	def __str__(self):
		return self.title