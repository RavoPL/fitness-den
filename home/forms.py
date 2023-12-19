from django import forms
from .models import SendContact

class ContactForm(forms.ModelForm):
    class Meta:
        model = SendContact
        fields = ['subject', 'message']