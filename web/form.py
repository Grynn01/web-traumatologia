from django import forms
from .models import Assistant, Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("nombre", "email", "mensaje",)
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'ej: Marcelo Gonzalez'}),
            'email': forms.TextInput(attrs={'placeholder': 'ej: marcelogon@gmail.com'}),
        }
