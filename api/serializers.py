from rest_framework import serializers
from .models import Role, Person


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ("name", "role_alias")


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("name", "email", "address")
