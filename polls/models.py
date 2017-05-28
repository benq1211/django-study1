from django.db import models
from django.utils import timezone
import datetime
import time
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
   
    def __str__(self):
       return self.question_text
    def was_published_recently(self):
       return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
   question = models.ForeignKey(Question,related_name='choices',on_delete=models.CASCADE)  
   choice_text=models.CharField(max_length=200)
   votes= models.IntegerField(default=0)
   

   def __str__(self):
        return self.choice_text
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return self.name
TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
class Author(models.Model):
    name = models.CharField(max_length=100,default="benq")
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, default="a" )
    birth_date = models.DateField(blank=True, null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=100,default="book")
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.name

