from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DataTimeField('data published')
class Choice(models.Model):
    question = models.CharField(max_length=200)
    votes = models.IntergerField(default=0)
