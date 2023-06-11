from django.contrib import admin
from .models import News,  Galery, Application,Calendar

# Register your models here.

admin.site.register(News)
admin.site.register(Galery)
admin.site.register(Application)
admin.site.register(Calendar)

