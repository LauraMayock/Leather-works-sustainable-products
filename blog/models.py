from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Main blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name




    