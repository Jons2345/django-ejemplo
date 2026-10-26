from django.conf import settings      # para leer las variables de settings.py


# Un context processor es una función que recibe la petición y devuelve un diccionario.
# Django la ejecuta en CADA página: así {{ NOMBRE_SISTEMA }} existe en todos los
# templates sin tener que enviarlo desde cada vista.
def datos_sistema(request):
    return {
        "NOMBRE_SISTEMA": settings.NOMBRE_SISTEMA,
        "EMPRESA": settings.EMPRESA,
        "VERSION_SISTEMA": settings.VERSION_SISTEMA,
    }