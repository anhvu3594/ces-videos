Django - Docker

Steps to start a project with Django using Docker within the workflow. It is used projectnameto refer to the name of the project.

Prerequisite

Have Docker installed . If you are using Mac OS X install Docker Toolbox .
Step One - Establish Structure.

Download project structure

The project that contains the general structure is downloaded.

git clone https://github.com/mmorejon/docker-django.git projectname
Remove Git folder

The folder .gitis deleted to create a new repository.

cd projectname
rm -rf .git/
Create new repository within the project

Version control is started within the project folder to record the changes.

git init
Step Two - Create Image by Docker

Create Image in Docker

The Docker image is created for the project. The image will contain the installation of the requirements established in the file requirements.txt.

The file requirements.txtcontains the basic requirements for starting and deploying an application with Django, if you need to add new elements this is a good time.

docker build -t projectname:1.0 .
Whenever you modify the elements within the file you requirements.txthave to repeat this step.

Configure Docker Compose

In the file docker-compose.ymlthe name of the image to be used is modified. The name of the image has been set in the previous step. The zone that is modified within the file is the following one:

image: projectname:1.0
Step Three - Create Django Project

Create Project The project is created using the same commands described by the Django site.

docker-compose run web django-admin startproject projectname .
Testing the system To test if the system is operating correctly, the following command is executed. In the browser you can review the application at the following address http://<ip-machine:8000>. The output port can be configured in the filedocker-compose.yml.

docker-compose up
For the system The system is stopped if necessary to continue with the settings.

Ctrl-C
Step Four - Create Application

To create an application within the Django project, use the following command:

docker-compose run web python manage.py startapp app
Step Five - Create User

Users are created using the same command described in the Django documentation.

docker-compose run web python manage.py createsuperuser
Step Six - Production Environment

To use the application in the production environment the following files must be configured:

Add projectname/settings.pythe following line to the end of the file :

STATIC_ROOT = './static/'
Add the line command: ./run-production.shto the file docker-compose.ymlas follows:

web:
  image: projectname:1.0
  command: ./run-production.sh
  volumes:
    - .:/code
  ports:
    - "8000:80"
Finally, you must modify the project name projectnamein the file conf/app.ini.

Related Links



* <a target="_blank" href="https://docs.docker.com/compose/django/">Docker Compose con proyectos Django</a>
* <a target="_blank" href="https://docs.djangoproject.com/es/1.9/intro/tutorial01/">Primeros pasos en projectos con Django</a>
