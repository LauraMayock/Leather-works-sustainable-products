from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path("contact", views.contact, name="contact"),
    path('faqs', views.Faqs.as_view(), name='faqs'),
    path('add_post/', views.AddPost, name='add_post'),
    path('update_post/<post_id>', views.update_post, name='update_post'),
    path('delete_post/<post_id>', views.delete_post, name='delete_post'),
    path('sustainable_leather', views.sustainable_leather, name='sustainable_leather'),
    path('meet_the_tanner', views.meet_the_tanner, name='meet_the_tanner'),
    path('certs', views.certs, name='certs'),
    path('custom', views.custom, name='custom'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
