from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'
