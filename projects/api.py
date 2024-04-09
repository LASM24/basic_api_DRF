from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


""" documentacion """

# se importa el modelo, los modulo "viewset" y"permissions" y el serializer
# creado anteriomente

# luego, se crea una clase (ProjectViewSet) la cual hereda de un modelo
# proviniente del modulo viewset y dentro de esta clase se define que consultas
# se podrán hacer (en este caso todos los objetos del modelo Project).
# tambien se definen los permisos, en este caso se habilita a todos
# (permissions.AllowAny), pero, se puede limitar las personas que podrán
# hacer las consultas a la web API.
# tambien se crea un "serializer_class" que define a partir de que serializer
# se harán las consultas


""" definiciones """
# 1) viewset: este modulo proporciona clases ya definidas con metodos accesores
# que facilitan la creacion del CRUD

# 2) permissions: este modulo ayuda con la identificacion de las clientes REST
# que quieran usar la API y definir que permisos posee cada uno.
