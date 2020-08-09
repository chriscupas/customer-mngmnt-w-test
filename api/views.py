from rest_framework import viewsets
from .serializers import RoleSerializer, PersonSerializer
from .models import Role, Person


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by("name")
    serializer_class = RoleSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("name")
    serializer_class = PersonSerializer
