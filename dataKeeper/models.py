from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    
    newsTitle = models.CharField(max_length=300)
    newsContent = models.TextField(null=True)
    newsImage = models.ImageField() 
    newsEventName = models.CharField(max_length=255)
    
    def __str__(self):
        return self.newsTitle
    
class Galery(models.Model):
    galeryGroup = models.CharField(max_length=100)
    galeryImage = models.ImageField(max_length=255)
    
class Application(models.Model):
    applicationUserName = models.CharField(max_length=255)
    applicationPhone = models.CharField(max_length=255)
    applicationTelegramm = models.CharField(max_length=255)
    applicationStudentsGroup = models.CharField(max_length=255)
    applicationDirection = models.CharField(max_length=255)
    applicationDescriptionDirection = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.applicationUserName    
    
     
class Calendar(models.Model):
    calendarEventTitle = models.CharField(max_length=255)
    calendarEventImage = models.ImageField(max_length=255)
    calendarEventDateNORMAL = models.CharField(max_length=255)
    calendarEventDateUNIX = models.CharField(max_length=255)
    
    def __str__(self):
        return self.calendarEventTitle    