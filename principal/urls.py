from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, index, detalle_post


urlpatterns = [
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('index/', index, name='posts'),
    path('detalle_post/', detalle_post, name='post'),
]