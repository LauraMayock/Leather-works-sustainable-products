from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path("contact", views.contact, name="contact"),
    path('faqs', views.Faqs.as_view(), name='faqs'),
    path('update_post/<post_id>', views.update_post, name='update_post'),
    path('delete_post/<post_id>', views.delete_post, name='delete-post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
