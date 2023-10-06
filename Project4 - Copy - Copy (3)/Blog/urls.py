from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.registerPage, name = 'register'),
    path('login/',views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('', views.retrieve_blog, name = 'retrieve-blog'),
    path('update/<int:pk>', views.update_blog, name = 'update-blog'),
    path('delete/<int:pk>', views.delete_blog, name = 'delete-blog'),
    path('add/', views.add_blog, name = 'add-blog')
]
