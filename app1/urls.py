from django.urls import path
from .views import *
app_name='course2'
urlpatterns = [
    path('devops/', devops, name='app1_page1'),
    path('Dev/', dev, name='app1_page2'),
    
]
