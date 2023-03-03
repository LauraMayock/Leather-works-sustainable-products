from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review

class NewProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        categories = Category.objects.all()
        firendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = firendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Uses Django form to enable users
    to add product reviews within
    Post Detail view.
    """
    class Meta:
        model = Review
        fields = ('message',)