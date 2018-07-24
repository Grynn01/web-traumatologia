from django.shortcuts import render, redirect
from .models import *
from smail import send_mail
# Create your views here.


def index(request):
    cursos = Course.objects.filter(activo=True)
    return render(request, 'web/index.html', {'cursos': cursos})


def signup_new(request):
    cursos = Course.objects.filter(activo=True)
    if request.method == "POST":
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        telefono = request.POST['telefono']
        email = request.POST['email']
        area_de_trabajo = request.POST['area_de_trabajo']
        lugar_de_trabajo = request.POST['lugar_de_trabajo']
        asistente, new_asistente = Assistant.objects.update_or_create(nombres=nombres, apellidos=apellidos,
                                                                      telefono=telefono, email=email,
                                                                      area_de_trabajo=area_de_trabajo,
                                                                      lugar_de_trabajo=lugar_de_trabajo)
        curso = Course.objects.get(id=request.POST['curso_elegido'])

        inscripcion, new_inscripcion = Inscription.objects.update_or_create(asistente=asistente, curso=curso)
        send_mail(email)
        return redirect('signup done')
    else:
        return render(request, 'web/index.html', {'cursos': cursos})


def signup_done(request):
    cursos = Course.objects.filter(activo=True)
    return render(request, 'web/signup_done.html', {'cursos': cursos})


def contact_new(request):
    cursos = Course.objects.filter(activo=True)
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        contacto, new_contacto = Message.objects.update_or_create(nombre=nombre, email=email, mensaje=mensaje)
        return redirect('contact done')
    else:
        return render(request, 'web/index.html', {'cursos': cursos})


def contact_done(request):
    cursos = Course.objects.filter(activo=True)
    return render(request, 'web/contact_done.html',  {'cursos': cursos})
