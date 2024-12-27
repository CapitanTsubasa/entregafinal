from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable, Post


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'principal/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'principal/estudiante_detail.html', {'estudiante': estudiante})

def index(request):
    posts = Post.objects.all()
    return render(request, 'principal/index.html', {'posts': posts})

def detalle_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'principal/detalle_post.html', {'post': post})