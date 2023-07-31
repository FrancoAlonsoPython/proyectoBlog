from django.urls import path
from .views import *




urlpatterns = [
   
    path('menu/', menu, name='menu'),
    path('sobreMi/', sobreMi, name='sobreMi'),
    path('blog/', blog, name='blog'),
    path('contacto/', contacto, name='contacto'),
    path('perfil/', perfil , name='perfil') ,
    path('<int:pk>', AutorDetalle.as_view(), name='Detail'),
    path('borar/<int:pk>', AutorDelete.as_view(), name='Delete'),
    path('editar/<int:pk>', AutorUpdate.as_view(), name='Edit'),
    path('nuevo/', AutorCreacion.as_view(), name='New'),
    path('autor/list/', AutorList.as_view(), name='autor_list'),
    path('perfil/', perfilview, name="perfil"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('changePassword/', changePassword, name="changePassword"),
    path('changeAvatar/', editAvatar, name="editAvatar"),
]