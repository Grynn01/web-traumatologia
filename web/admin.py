from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
# Register your models here.


class AssistantAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'telefono', 'email')
    list_filter = ('apellidos', 'nombres')
    ordering = ('-apellidos',)
    search_fields = ['apellidos', 'nombres']


class MessageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'date')
    ordering = ('-date',)
    search_fields = ['nombre', 'email']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    ordering = ('-fecha',)
    search_fields = ['nombre', 'fecha']

"""


class InscriptionResource(resources.ModelResource):
    asistente = fields.Field(
        column_name='Apellidos',
        attribute='asistente',
        widget=ForeignKeyWidget(Assistant, 'apellidos'))
    nombres = fields.Field(
        column_name='Nombres',
        attribute='asistente',
        widget=ForeignKeyWidget(Assistant, 'nombres'))
    emails = fields.Field(
        column_name='emails',
        attribute='asistente',
        widget=ForeignKeyWidget(Assistant, 'email'))
    curso = fields.Field(
        column_name='Curso',
        attribute='curso',
        widget=ForeignKeyWidget(Course, 'nombre'))
    date = fields.Field(
        column_name='Fecha',
        attribute='curso',
        widget=ForeignKeyWidget(Course, 'fecha'))

    class Meta:
        fields = ('nombres', 'emails')
        exclude = ('id',)
        model = Inscription


class InscriptionAdmin(ImportExportModelAdmin):
    list_display = ('asistente', 'curso')
    list_filter = ('asistente', 'curso')
    ordering = ('-date',)
    resource_class = InscriptionResource
    
    
admin.site.register(Inscription, InscriptionAdmin)

"""

admin.site.register(Assistant, AssistantAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Course, CourseAdmin)


