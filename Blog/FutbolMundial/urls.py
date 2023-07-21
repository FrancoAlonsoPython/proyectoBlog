from django.urls import path
from .views import *



urlpatterns = [
   
    path('menu/', menu, name='menu'),
    path('sobreMi/', sobreMi, name='sobreMi'),
    path('blog/', blog, name='blog'),
    path('contacto/', contacto, name='contacto'), 
]