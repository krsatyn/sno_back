import datetime
import time

def unix_convertor(date): 
        stringListCalendarEventDate = date
        
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
    
#a = unix_convertor("2022-03-31 14:11")
#print(type(a))


from settings import MEDIA_ROOT

a = r'^media/(?P<path>.*)$'
b = MEDIA_ROOT
print(a, b)
