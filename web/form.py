from django import forms
from .models import Assistant, Message


class AssistantForm(forms.ModelForm):
    class Meta:
        model = Assistant
        fields = ("nombres", "apellidos", "telefono", 'email',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("nombre", "email", "mensaje",)



