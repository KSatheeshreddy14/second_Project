from django.urls import path
from app2.views import *

app_name = 'courses'  

urlpatterns = [
    path('python/', python, name='python'),
    path('sql/', sql, name='sql'),
    path('dummy/',dummy,name='dummy')
]
