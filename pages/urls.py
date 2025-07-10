from django.urls import URLPattern, path
from pages import views  #from this app import views

urlpatterns = [
    path('home/', views.home_view, name='home_page'),
    path('', views.about_me_view, name= 'about_me'),

]