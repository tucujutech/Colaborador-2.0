from django.conf.urls import url
from .views import *

urlpatterns=[
   url('usernew/', resistrarUsuario, name='usernew'),
   url('dashboard/', dashboard, name='dashboard'),
   url('login/',Login,name='login'),
   url(r'^logout/',deslogar,name='logout'),
   url(r'^listuser/',ListarUsuario,name='listuser'),
   url(r'^colaboradorNew/', ColaboradorNew, name='colaboradorNew'),
   url(r'^listarColaborador/', ListarColaborador, name='listarColaborador'),
   url('^formacaoNew/', FormacaoNew, name='formacaoNew'),
   url('^listarFormacao', ListarFormacao, name='listarFormacao'),
]