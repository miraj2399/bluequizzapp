from django.db import models
from django.contrib.auth.models import User
from django.http import request
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=10000)
    option_1= models.CharField(max_length=10000)
    option_2= models.CharField(max_length=10000)
    option_3= models.CharField(max_length=10000)
    option_4= models.CharField(max_length=10000)
    option_correct = models.IntegerField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,default = None, null = True)

class Quiz(models.Model):
    questions = models.ManyToManyField(Question)
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default = None, null = True)
    
