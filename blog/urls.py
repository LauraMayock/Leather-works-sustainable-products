from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path("contact", views.contact, name="contact"),
    path('faqs', views.Faqs.as_view(), name='faqs'),
]
