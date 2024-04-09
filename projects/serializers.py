from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)


""" Documentacion """
# se importa el modelo para que DRF sepa que tipo de dato va a retornar,
# en este caso, una(s) instancia(s) del modelo Project creado anteriormente.

# luego, se crea una clase la cual convierte ese modelo a datos que podrá ser
# consultados (ProjectSerializer) con una meta clase (Meta) la cual define:
# 1) el modelo que se usará. 2) los campos a consultar. 3) define que campos
# serán de solo lectura.


""" definiciones """
# serializer: es el "puente" que genera la union y conversion entre las
# instancias de un modelo (Project en este caso) con el formato que se usará
# para el envio o recibimiento de datos.
