from .models import *
from rest_framework import serializers
from django.core import serializers as sz
import json
from django.db import connection
class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many = True)
    clients = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = '__all__'
    def get_clients(self, obj):
        print(obj.id)
        project_clients = Client.objects.raw('Select * from employees_client join employees_project on employees_client.id = employees_project.id')
        return sz.serialize('json', project_clients)
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class ProjectEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectEmployee
        fields = '__all__'