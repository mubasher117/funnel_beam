Technology used : Django Rest Framework

Installation:
	pip install django
	pip install djangorestframework

Running app:
	In folder containing file 'manage.py', run command: 
	python manage.py runserver

Running Test Suite:
	Authorization Token : a0009e19e807f873d87b6cdad585b28e665dbaf9
	API : /client
		Adds or removes clients.
		GET: 
			returns all clients with their projects and employees associated with their projects.
		POST:
			{"name" : "Ahmad"}
		PUT: 
			{"client_id": 1, "new_name" : "Irfan"}
		DELETE:
			{"client_id": 1 }
	API: /client?client_id=4
		GET: returns client with id 4

	API : /project
		Adds or removes projects of the clients
		GET: 
			returns all projects
		POST:
			{"title" : "Web App", "client_id": 1}
		PUT: 
			{"project_id": 1, "new_title" : "Mobile App", "new_owner": 2}
		DELETE:
			{"project_id": 1 }
	API: /project?project_id=4
		GET: returns project with id 4

	API : /employee
		Adds or removes employees
		GET: 
			returns all employees
		POST:
			{"name" : "Ahmad"}
		PUT: 
			{"employee_id": 1, "new_name" : "Irfan"}
		DELETE:
			{"employee_id": 1 }
	API: /employee?employee_id=4
		GET: returns employee with id 4


	API : /proj_emp
		Assigns or removes employees to the projects
		GET: 
			returns all employees associated with the project
		POST:
			{"project_id" : 1, "employee_id": 1}
		DELETE:
			{"project_id": 1, "employee_id": 1 }
