# Notes

## Python Virtual Environment (VENV)

A virtual environment is used to manage this project's dependencies separately from other projects. It's installed outside the synchronized project folder to ensure it isn't deleted if the project files are.

The environment is located in the Docker container's home directory.
See cheat sheet
<https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/>

### Creation

```bash
python3 -m venv ~/env
```

### Activation

```bash
source ~/env/bin/activate
```

Your terminal prompt will change to show that the environment is active.

### Deactivation

```bash
deactivate
```

--------

## Install Required Python Packages

### Creating requirements file

It's best practice to list all of the required Python Packages in a file called `requirements.txt`.
We list all the required packages as well as the version.

```txt
django==2.2
djangorestframework==3.9.2
```

These packages are not updated for 2025, but I kept them for the sake of following the videos.
To update versions I can go to https://pypi.org.

### Installing requirements in Python virtual environment

1. Make sure we're on the project's folder in the dev server.

2. Make sure the venv is activated. (`source ~/env/bin/activate`).
3. Install requirements from requirements file: 

   ```bash
   pip install -r requirements.txt 
   ```

--------

## Create a New *Django* Project and App

### Create Django Project

Create a new Django project, with the name `profile_projects` in location `.` (root of project).

```bash
django-admin.py startproject profiles_project .
```

It created a new folder called `profiles_project`, and `manage.py` script. 

### Create Django App

A project can consist of multiple sub applications for different functionalities. 

```bash
python manage.py startapp profiles_api
```

### Enable App in *Django* Settings

We need to enable our new `profiles_api` app in the Django project.

1. Open the Django settings file:  
   `profiles_project/settings.py`

2. Locate the `INSTALLED_APPS` list.  
   This list contains all apps that Django will use. Apps can come from:
   - Installed packages via `requirements.txt`
   - Locally created apps

3. Add the following lines to `INSTALLED_APPS` to enable the new app and required Django REST Framework features:

```python
'rest_framework',
'rest_framework.authtoken',
'profiles_api',
```

### Test Changes

Testing changes in the browser, using the Django developer server.

#### Start *Django* Developer Server

Make sure you're in the docker container, with python environment activated. Then run:

```bash
python manage.py runserver 0.0.0.0:8000
```

To stop the server: `CTRL-C`.

--------

## Django Models

See [documentation](https://docs.djangoproject.com/en/1.11/topics/db/models/).

- Model: A Python class that defines your data structure.

- Database Table: The storage location for your data, automatically created from your model.

- Object-Relational Mapper (ORM): The built-in Django feature that translates your model code into database operations (e.g., creating, reading, updating, and deleting records), eliminating the need for manual SQL.

### Creating User Profile Model 

We're overriding the default user model by Django with our own custom model, that allows \
to **use an email address** instead of the standard username that comes with the default model.

Best practice - keep all models in the file `profiles_api/models.py`.

```python
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
```

