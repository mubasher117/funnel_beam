from .models import *
from rest_framework import serializers
from django.core import serializers as sz
import json
from django.db import connection


class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True)
    clients = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'

    def get_clients(self, obj):
        #Returns a serialized list of names of employees related to the client
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT DISTINCT e.name FROM employees_project as p join employees_projectemployee as pe on p.id = pe.project_id join employees_employee as e on pe.employee_id= e.id where p.owner_id = %s ; ", [obj.id])
            row = cursor.fetchall()
        employees_names = []
        for employee in row:
            employees_names.append(employee[0])
        return json.dumps(employees_names)


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
