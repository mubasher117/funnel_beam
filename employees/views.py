from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
import json


class ClientsList(APIView):
    def get(self, request):
        clients_data = request.query_params
        client_id = clients_data.get('client_id')
        client_profile = None
        if client_id == None:
            client_profile = Client.objects.all()
            print(client_profile.query)
        else:
            client_profile = Client.objects.filter(id=client_id)
        serializer = ClientSerializer(client_profile, many=True)
        """
        names = []
        for client in client_profile:
            names.append(client.name)
        return Response(json.dumps(names))
        """
        return Response(serializer.data)

    def post(self, request):
        client_data = request.data
        name = client_data.get('name')
        Client.objects.create(name=name)
        return Response(200)
    def delete(self, request):
        client_data = request.data
        client_id = client_data.get('client_id')
        try:
            client = Client.objects.get(id=client_id)
        except:
            return Response("No client with this id available")
        client.delete()        
        return Response(200)
    def put(self, request):
        client_data = request.data
        client_id = client_data.get('client_id')
        client_new_name = client_data.get('new_name')
        try:
            client = Client.objects.get(id=client_id)
        except:
            return Response("No client with this id available")
        client.name = client_new_name
        client.save()
        return Response(200)

        


class ProjectList(APIView):
    def get(self, request):
        project_data = request.query_params
        project_id = project_data.get('project_id')
        project_profile = None
        if project_id == None:
            project_profile = Project.objects.all()
        else:
            project_profile = Project.objects.filter(id=project_id)
        serializer = ProjectSerializer(project_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        project_data = request.data
        title = project_data.get('title')
        client_id = project_data.get('client_id')
        try:
            owner = Client.objects.get(id=client_id)
        except:
            return Response("No client with this id available")
        Project.objects.create(title=title, owner=owner)
        return Response(200)
    def delete(self, request):
        project_data = request.data
        project_id = project_data.get('project_id')
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response("No project with this id available")
        project.delete()        
        return Response(200)
    def put(self, request):
        project_data = request.data
        project_id = project_data.get('project_id')
        project_new_title = project_data.get('new_title')
        project_new_owner = project_data.get('new_owner')
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response("No project with this id available")
        if project_new_title != None:
            project.title = project_new_title
        if project_new_owner != None:
            try:
                client = Client.objects.get(id=project_new_owner)
                project.owner = client
            except:
                return Response("No client with this id available")
        project.save()
        return Response(200)
    



class EmployeeList(APIView):
    def get(self, request):
        employee_data = request.query_params
        employee_id = employee_data.get('employee_id')
        employee_profile = None
        if employee_id == None:
            employee_profile = Employee.objects.all()
        else:
            employee_profile = Employee.objects.filter(id=employee_id)
        serializer = EmployeeSerializer(employee_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        employe_data = request.data
        name = employe_data.get('name')
        Employee.objects.create(name=name)
        return Response(200)
    def delete(self, request):
        employee_data = request.data
        employee_id = employee_data.get('employee_id')
        try:
            employee = Employee.objects.get(id=employee_id)
        except:
            return Response("No employee with this id available")
        employee.delete()        
        return Response(200)
    def put(self, request):
        employee_data = request.data
        employee_id = employee_data.get('employee_id')
        employee_new_name = employee_data.get('new_name')
        try:
            employee = Employee.objects.get(id=employee_id)
        except:
            return Response("No employee with this id available")
        employee.name = employee_new_name
        employee.save()
        return Response(200)


class ProjectEmployeeList(APIView):
    def get(self, request):
        project_employee_data = request.query_params
        project_id = project_employee_data.get('project_id')
        employee_id = project_employee_data.get('employee_id')
        project_employee_profile = None
        if project_id == None and employee_id == None:
            project_employee_profile = ProjectEmployee.objects.all()
        elif project_id == None:
            project_employee_profile = ProjectEmployee.objects.filter(
                employee=employee_id)
        elif employee_id == None:
            project_employee_profile = ProjectEmployee.objects.filter(
                project=project_id)
        else:
            project_employee_profile = ProjectEmployee.objects.filter(
                project=project_id, employee=employee_id)
        serializer = ProjectEmployeeSerializer(
            project_employee_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_data = request.data
        project_id = request_data.get('project_id')
        employee_id = request_data.get('employee_id')
        try:
            project = Project.objects.get(id=project_id)
        except:
            return Response("No project with this id available")
        try:
            employee = Employee.objects.get(id=employee_id)
        except:
            Response("No employee available with this id")
        ProjectEmployee.objects.create(project=project, employee=employee)
        return Response(200)

    def delete(self, request):
        project_employee_data = request.data
        project_id = project_employee_data.get('project_id')
        employee_id = project_employee_data.get('employee_id')
        try:
            project = Project.objects.get(id=project_id)
            employee = Employee.objects.get(id=employee_id)
            project_employee = ProjectEmployee.objects.get(project = project, employee = employee)
        except:
            return Response("No employee or project with this id available")
        project_employee.delete()        
        return Response(200)
