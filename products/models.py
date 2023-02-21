from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MaxValueValidator,MinValueValidator

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categoies'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    color_choice = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_url_2 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_3 = models.URLField(max_length=1024, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=1024, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    
    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"

    
class Review(models.Model):
    """
    Models the fields for adding product reviews.
    """
    User = get_user_model()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='user_reviews')
    message = models.TextField(help_text='Add your review here')
    rating = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review {self.message} by {self.username}'