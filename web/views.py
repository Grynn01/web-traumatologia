from django.shortcuts import render, redirect
from .form import AssistantForm, MessageForm

# Create your views here.


def index(request):
    return render(request, 'web/indexres.html')


def info(request):
    return render(request, 'web/info.html')


def itinerario(request):
    return render(request, 'web/itinerario.html')


def signup_new(request):
    if request.method == "POST":
        form = AssistantForm(request.POST)
        if form.is_valid():
            assist = form.save(commit=False)
            assist.save()
            return redirect('signup done')
    else:
        form = AssistantForm()
    return render(request, 'web/signup_new.html', {'form': form})


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
