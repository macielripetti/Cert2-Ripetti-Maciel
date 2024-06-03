from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Proyecto, Tema
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal después del inicio de sesión
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return redirect(proyecto)

def proyecto(request: HttpRequest):
    tema_id = int(request.GET.get('id', 0))

    proyectos = Proyecto.objects.filter(tema_id=tema_id) if tema_id else Proyecto.objects.all()
    temas = Tema.objects.all()

    return render(
        request, 
        'comunicados/home.html',
        context={
            'proyectos': proyectos,
            'temas': temas,
            'id_tema_actual': tema_id
        },)

@login_required
def crear(request):
    if request.method == 'POST':
        nombrep = request.POST['txtNombre']
        estudiante = request.POST['txtEstudiante']
        email = request.POST['txtEmail']
        tema = request.POST['cboTema']
        descripcion = request.POST['txtDescripcion']

        nuevo_proyecto = Proyecto(
            nombrep=nombrep,
            estudiante=estudiante,
            email=email,
            tema=tema,
            descripcion=descripcion
        )
        nuevo_proyecto.save()

    return render(request, 'comunicados/crear.html')

@login_required
def listar(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'comunicados/editar.html', {'proyectos': proyectos})

@login_required
def editar(request, nombrep):
    proyecto = get_object_or_404(Proyecto, nombrep=nombrep)

    if request.method == 'POST':
        proyecto.nombrep = request.POST.get('txtNombre', proyecto.nombrep)
        proyecto.estudiante = request.POST.get('txtEstudiante', proyecto.estudiante)
        proyecto.email = request.POST.get('txtEmail', proyecto.email)
        proyecto.tema = request.POST.get('cboTema', proyecto.tema)
        proyecto.descripcion = request.POST.get('txtDescripcion', proyecto.descripcion)
        proyecto.save()
        return redirect('editar')  # Redirigir a la lista de proyectos después de guardar

    return render(request, 'comunicados/editarproyecto.html', {'proyecto': proyecto})


@login_required
def mostrar_proyectos(request):
    tiene_profesor = request.GET.get('tiene_profesor')
    if tiene_profesor == 'asignado':
        proyectos = Proyecto.objects.exclude(profesor__isnull=True).exclude(profesor__exact='')
    elif tiene_profesor == 'no_asignado':
        proyectos = Proyecto.objects.filter(profesor__isnull=True) | Proyecto.objects.filter(profesor__exact='')
    else:
        proyectos = Proyecto.objects.all()
    return render(request, 'comunicados/asignado.html', {'proyectos': proyectos, 'tiene_profesor': tiene_profesor})

@login_required
def asignar_profesor(request, nombrep):
    if request.method == 'POST':
        proyecto = get_object_or_404(Proyecto, nombrep=nombrep)
        if not proyecto.profesor:
            proyecto.profesor = request.user.username
            proyecto.save()
            return JsonResponse({'success': True, 'profesor': proyecto.profesor})
    return JsonResponse({'success': False})

@login_required
def proyecto_tiene_profesor(request):
    tema = request.GET.get('tema')
    if tema:
        proyectos = Proyecto.objects.exclude(profesor__isnull=True).exclude(profesor__exact='').filter(tema=tema)
    else:
        proyectos = Proyecto.objects.exclude(profesor__isnull=True).exclude(profesor__exact='')
    return render(request, 'comunicados/home.html', {'proyectos': proyectos, 'tema': tema})



