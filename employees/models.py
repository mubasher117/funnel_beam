from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Client, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=100)


class ProjectEmployee(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
