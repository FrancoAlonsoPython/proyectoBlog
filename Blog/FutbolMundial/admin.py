from django.contrib import admin
from FutbolMundial.models import Autores,Comentario
from django.contrib.admin.models import LogEntry
from .models import *
# Register your models here.

admin.site.register(Autores)
admin.site.register(Comentario)
admin.site.register(LogEntry)
admin.site.register(Avatar)