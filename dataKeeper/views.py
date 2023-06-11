from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import *
from .serializer import *
#библиотека для unix
import datetime
import time

PATH_IMAGE = "http://snoo.aleksbcg.beget.tech/media/"

class NewsData(APIView):

    
    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get("pk", None)
        if not pk:
            lst = News.objects.all().values()
            return Response(lst)
        
        proj = News.objects.filter(id=self.kwargs['pk']).values()
        promArr = []
        for pr in proj:
            if pr['id'] != 0:
                promArr.append(pr)

        return Response(promArr)
    
    def rename_image(self, image_name):
        path_image = PATH_IMAGE

        new_name = path_image + image_name
        
        return(new_name)
    
    def post(self, request):
        newPost = News.objects.create(
            newsTitle=request.data['newsTitle'],
            newsContent=request.data['newsContent'],
            newsImage=self.rename_image(request.data['newsImage']),
            newsEventName=request.data['newsEventName'],
        )
        return Response("news successfully added")
    #нет возможности изменить фото
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk not define"})

        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
            
        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            return Response({"error":"pk not define"})
        
        try:
            isinstance = News.objects.get(pk=pk)
            isinstance.delete()
        except:
            return(Response({"error": "Methon DELETE not allowed"}))
        
        return Response({"Выкинуто на орбиту": "ид:" + str(pk)})
        
class GaleryData(APIView):

    def get(self, request):
        lst = Galery.objects.all().values()
        return Response(lst)

    def post(self, request):
        newPost = Galery.objects.create(
            galeryGroup=request.data['galeryGroup'],
            galeryImage=request.data['galeryImage'],
        )
        return Response("Photo successfully added")
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk not define"})

        try:
            instance = Galery.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
            
        serializer = GalerySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            return Response({"error":"pk not define"})
        
        try:
            isinstance = Galery.objects.get(pk=pk)
            isinstance.delete()
        except:
            return(Response({"error": "Methon DELETE not allowed"}))
        
        return Response({"Выкинуто на орбиту": "ид:" + str(pk)})
    
class ApplicationData(APIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
    def get(self, request):
        lst = Application.objects.all().values()
        return Response(lst)

    def post(self, request):
        newPost = Application.objects.create(
            applicationUserName=request.data['applicationUserName'],
            applicationPhone=request.data['applicationPhone'],
            applicationTelegramm=request.data['applicationTelegramm'],
            applicationStudentsGroup=request.data['applicationStudentsGroup'],
            applicationDirection=request.data['applicationDirection'],
            applicationDescriptionDirection=request.data['applicationDescriptionDirection'],
        )
        print("qwer")
        return Response("Application successfully added")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk not define"})

        try:
            instance = Application.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
            
        serializer = ApplicationSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            return Response({"error":"pk not define"})
        
        try:
            isinstance = Application.objects.get(pk=pk)
            isinstance.delete()
        except:
            return(Response({"error": "Methon DELETE not allowed"}))
        
        return Response({"Выкинуто на орбиту": "ид:" + str(pk)})
    
class CalendarData(APIView):

    def get(self, request):
        lst = Calendar.objects.all().values()
        return Response(lst)

    def unix_convertor(self, date): 
        stringListCalendarEventDate = date
        """ 2023-10-12 13:12"""
        #разбиваем год-мм-дд чч:мн на 2 отдельных списка
        stringListCalendarEventDate = stringListCalendarEventDate.split(" ")
        
        #разибваю подаваемую строку на заранее заготовленные позиции (мы знаем что разделяемый символ "-" и ":")
        stringListCalendarEventDate = stringListCalendarEventDate[0].split("-") + stringListCalendarEventDate[1].split(":")
        
        #переводим в DATATIME 
        #позиция такая [0]-год/[1]-меся/[2]-номер дня/[3]-текущий час/[4]-текущие минуты ()изначально данные в строке их надо отИнтевать по мужски
        unix_calendarEventDate = datetime.datetime(int(stringListCalendarEventDate[0]), int(stringListCalendarEventDate[1]), 
                                                   int(stringListCalendarEventDate[2]), int(stringListCalendarEventDate[3]), 
                                                   int(stringListCalendarEventDate[4]))
        
        #перевод в unix
        unix_calendarEventDate = time.mktime(unix_calendarEventDate.timetuple())
        print("dfioevuegerhvbgjtrhultgudfibryefguketvteruybogvwthu", unix_calendarEventDate)
        
        return(unix_calendarEventDate)
    
    def rename_image(self, image_name):
        path_image = PATH_IMAGE

        new_name = path_image + image_name
        
        return(new_name)
     
    def post(self, request):
        
        
        unix_calendarEventDate = self.unix_convertor(request.data['calendarEventDateNORMAL'])
        
        newPost = Calendar.objects.create(
            calendarEventDateUNIX=unix_calendarEventDate,
            calendarEventTitle=request.data['calendarEventTitle'],
            calendarEventImage=self.rename_image(request.data['calendarEventImage']),
            calendarEventDateNORMAL=request.data['calendarEventDateNORMAL']
        )
        
        return Response("Calendar successfully added")
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk not define"})

        try:
            instance = Calendar.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
            
        serializer = CalendarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            return Response({"error":"pk not define"})
        
        try:
            isinstance = Calendar.objects.get(pk=pk)
            isinstance.delete()
        except:
            return(Response({"error": "Methon DELETE not allowed"}))
        
        return Response({"Выкинуто на орбиту":"ид:" + str(pk)})