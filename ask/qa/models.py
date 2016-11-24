from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Class QuestionManager(models.Manager):
	def new(self):
		return self.objects.all()[:10]

	def popular(self):
		return self.objects.order_by('rating').all()
		
Class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)
	objects = QuestionManager
	Class Meta:
		ordering = ['-added_at']

Class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.OneToOneField(Question)
	author = models.ForeignKey(User)
	Class Meta:
		ordering = ['-added_at']