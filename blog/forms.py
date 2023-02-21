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


# Form for user to create a book review.
class CreatePost(forms.ModelForm):
    """
    Creates a form based on the Post model
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'snippet', 'content')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control',
                                        'label': 'name'}),
        'feature_image': forms.Select(attrs={'class': 'form-control'}),
        'snippet': forms.Select(attrs={'placeholder': 'snippet of blog'}),
        'content': forms.TextInput(attrs={'placeholder': 'blog post'}),
    }