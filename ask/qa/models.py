from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new(self):
		return self.objects.all()

	def popular(self):
		return self.objects.order_by('rating').all()
		
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)
	objects = QuestionManager()
	class Meta:
		ordering = ['-added_at']

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	question = models.OneToOneField(Question)
	author = models.ForeignKey(User)
	class Meta:
		ordering = ['-added_at']		