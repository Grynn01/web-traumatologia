from django.contrib import admin
from .models import Assistant, Message
from  django.db import models

# Register your models here.


class AssistantAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'telefono', 'email', 'date')
    list_filter = ('apellidos', 'nombres')
    ordering = ('-date',)
    search_fields = ['apellidos', 'nombres']


class MessageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'date')
    ordering = ('-date',)
    search_fields = ['nombre', 'email']


admin.site.register(Assistant, AssistantAdmin)
admin.site.register(Message, MessageAdmin)
