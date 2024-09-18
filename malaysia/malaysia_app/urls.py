from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
  
    #  path('about/', views.about, name='m-about'),
    #  path('login/',views.login, name='m-login'),
      # path('register/',views.register, name='m-register'),
    # path('about/', views.about, name='p-about'),

