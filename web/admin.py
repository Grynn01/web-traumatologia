from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, CharWidget, DateWidget, Widget
# Register your models here.


class AssistantAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'telefono', 'email')
    list_filter = ('apellidos', 'nombres')
    ordering = ('-apellidos',)
    search_fields = ['apellidos', 'nombres']


class MessageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'date', 'respondido')
    ordering = ('-date',)
    search_fields = ['nombre', 'email', 'respondido']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    ordering = ('-fecha',)
    search_fields = ['nombre', 'fecha']


class InscriptionResource(resources.ModelResource):
    apellido = fields.Field(
        column_name='Apellidos',
        attribute='asistente',
        widget=ForeignKeyWidget(Assistant, 'apellidos'))
    nombres = fields.Field(
        column_name='Nombres',
        attribute='asistente',
        widget=ForeignKeyWidget(Assistant, 'nombres'))
    emails = fields.Field(
        column_name='Emails',
        attribute='asistente',
        widget=ForeignKeyWidget(Assistant, 'email'))
    curso = fields.Field(
        column_name='Curso',
        attribute='curso',
        widget=ForeignKeyWidget(Course, 'nombre'))

    class Meta:
        fields = ()
        exclude = ('id',)
        model = Inscription


class InscriptionAdmin(ImportExportModelAdmin):
    list_display = ('asistente', 'curso', 'pagado')
    list_filter = ('asistente', 'curso', 'pagado')
    ordering = ('-date',)
    resource_class = InscriptionResource
    
    
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Assistant, AssistantAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Course, CourseAdmin)


