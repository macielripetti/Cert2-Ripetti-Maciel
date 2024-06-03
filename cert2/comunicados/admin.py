
from django.contrib import admin
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, Tema
from django.http import JsonResponse
# Register your models here.
from .models import Proyecto,Tema

admin.site.register(Proyecto)
admin.site.register(Tema)

