from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.start_project, name='main_page'),
    
]