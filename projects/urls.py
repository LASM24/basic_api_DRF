# This Python code snippet is setting up a REST API endpoint for
# projects using the Django
from rest_framework import routers
from .api import ProjectViewSet


router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls


""" documentacion """

# Se importan el módulo 'routers' de DRF junto al modelo que se usará
# para consultar.

# luego, se crea una variable la cual herede de la clase "DefaultRouter"
# que proviene del modulo routers.

# luego,se registra la url usando el metodo "register" el cual genera las rutas
# necesarias para el CRUD (GET, POST, DELETE, PUT) y a este metodo se le pasa
# la ruta, el modelo y el "nombre" para referenciarlo facilmente, algo bastante
# parecido a las urls de Django, pero, con diferentes funcionalidades y
# sintaxis diferente.

# luego, se usa el urlpatterns para generar las urls.
