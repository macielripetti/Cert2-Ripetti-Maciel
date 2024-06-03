from django.urls import path
from django.contrib import admin
from comunicados import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.proyecto_tiene_profesor, name="home"),
    path('crear/', views.crear, name="crear"),
    path('editar', views.listar, name='editar'),
    path('editar/<str:nombrep>/', views.editar, name='editar_proyecto'),
    path('asignado/', views.mostrar_proyectos, name="asignado"),
    path('asignar_profesor/<str:nombrep>/', views.asignar_profesor, name='asignar_profesor'),


]


