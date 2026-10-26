from django.conf import settings               # para leer DEBUG, MEDIA_URL y MEDIA_ROOT
from django.conf.urls.static import static     # entrega los archivos subidos mientras programas
from django.contrib import admin               # el panel de administración
from django.urls import include, path          # path = una ruta · include = "trae las rutas de otro archivo"

urlpatterns = [                                # Django revisa esta lista de arriba hacia abajo
    path("admin/", admin.site.urls),           # /admin/ → panel de administración
    path("cuentas/", include("django.contrib.auth.urls")),   # /cuentas/login/ y /cuentas/logout/
    path("", include("facturacion.urls")),     # todo lo demás lo resuelve nuestra app
]

# Solo en desarrollo (DEBUG = True): Django entrega los archivos de /media/.
# Los de /static/ ya los entrega runserver. En un servidor real lo hace Nginx o Apache.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)