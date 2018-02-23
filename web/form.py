from django import forms
from .models import Assistant, Message


class AssistantForm(forms.ModelForm):
    class Meta:
        model = Assistant
        fields = ("nombres", "apellidos", "telefono", 'email',)
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'ej: Juan Pedro'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'ej: Urrutia Gonzalez'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'ej: +569XXXXXXXX'}),
            'email': forms.TextInput(attrs={'placeholder': 'ej: urrutiagon@gmail.com'}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("nombre", "email", "mensaje",)
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'ej: Marcelo Gonzalez'}),
            'email': forms.TextInput(attrs={'placeholder': 'ej: marcelogon@gmail.com'}),
        }



