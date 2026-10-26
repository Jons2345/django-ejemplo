from django.contrib.auth.decorators import login_required   # obliga a iniciar sesión
from django.urls import path                                # función para declarar cada ruta
from django.views.generic import TemplateView               # vista que solo muestra un template

from . import views               # el punto = "de esta misma carpeta": facturacion/views.py

urlpatterns = [                   # aquí iremos agregando las rutas de cada CRUD
    # Página principal PROVISIONAL: solo muestra dashboard.html (todavía sin estadísticas).
    # En el módulo «Dashboard» la cambiarás por views.DashboardView.
    path("", login_required(TemplateView.as_view(template_name="facturacion/dashboard.html")),
         name="dashboard"),
]