from django.urls import include, path
from rest_framework import routers
from employees.views import *
from django.conf.urls import url
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'admin/', admin.site.urls),
    url(r'client', ClientsList.as_view()),
    url(r'project', ProjectList.as_view()),
    url(r'employee', EmployeeList.as_view()),
    url(r'proj_emp', ProjectEmployeeList.as_view()),
]