from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Class QuestionManager(models.Manager):
	def new(self):
		return self.objects.all()

	def popular(self):
		return self.objects.order_by('rating').all()
"""		
Class Question(models.Model):
	title = models.CharField()
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User,related_name='question_like_user')
#	objects = QuestionManager()
	Class Meta:
		ordering = ['-added_at']

Class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.OneToOneField(Question)
	author = models.ForeignKey(User)
	Class Meta:
		ordering = ['-added_at']		