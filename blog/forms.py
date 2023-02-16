from django import forms
from django.forms import ModelForm
from .models import Contact, Post


class ContactForm(ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'


# Form for user to create a book review.
class BlogPost(forms.ModelForm):
    """
    Creates a form based on the Post model
    """
    class Meta:
        model = Post
        fields = '__all__'
