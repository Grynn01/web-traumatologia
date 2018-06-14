from django.shortcuts import render, redirect
from .models import *
from .form import *

# Create your views here.


def index(request):
    return render(request, 'web/indexres.html')


def info(request):
    return render(request, 'web/info.html')


def itinerario(request):
    return render(request, 'web/itinerario.html')


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

        return redirect('signup done')
    else:
        return render(request, 'web/signup_new.html', {'cursos': cursos})


def signup_done(request):
    return render(request, 'web/signup_done.html')


def contact_new(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('contact done')
    else:
        form = MessageForm()
    return render(request, 'web/contact_new.html', {'form': form})


def contact_done(request):
    return render(request, 'web/contact_done.html')
