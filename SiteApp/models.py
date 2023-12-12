from django.db import models
from django.utils import timezone

class Services(models.Model):
    '''services table'''
    name = models.CharField(max_length=20)
    Orderdate = models.DateField()
    DueDate = models.DateField()

    class Meta:
        verbose_name_plural='Services'
       

    def __str__(self):
        return self.name

class Blogs(models.Model):
    '''blogs database'''
    title = models.CharField(max_length=100)
    pubDate = models.DateTimeField()
    text = models.TextField()
    tags = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural='Blogs'


    def __str__(self):
        return self.title

class Comment(models.Model):
    '''adding comments table for each blog'''
    title = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    authorEmail = models.EmailField()
    text = models.CharField(max_length=250)
    date = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.text

class Projects(models.Model):
    '''record of projects worked on'''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    url = models.URLField()
    git = models.URLField()
    startDate = models.DateField()
    finishDate = models.DateField()
    
    class Meta:
        verbose_name_plural='Projects'

    def __str__(self):
        return self.name
