from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("newsTitle", "newsContent", "newsImage", "newsEventName")
        
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("applicationUserName", "applicationPhone", "applicationTelegramm", 
                  "applicationStudentsGroup", "applicationDirection", "applicationDescriptionDirection")
        
class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = ("galeryGroup", "galeryImage")
        
class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ("calendarEventDateNORMAL","calendarEventDateUNIX", "calendarEventTitle", "calendarEventImage",)