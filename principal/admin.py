from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Entregable, Post

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Post)