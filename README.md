
To Demo the backend:

-Copy the repository
-Create local PostgreSQL database
- . .venv/bin/activate      to activate virtual enviroment
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver





***********Steps used to create backend*********
-Create Project Directory and Backend Directory
-Create Virtual Environment inside Backend Directory:
	Python -m venv .venv
-Activate Virtual Environment:
	. .venv/bin/activate
-Install Django:
	pip install Django
-Install Django REST Framework:
pip install Django -Install django-cors-headers:
	pip install django-cors-headers
-Install Psycopg and Psycopg-binary:
	pip install psycopg psycopg-binary
-Create Django Project:
	django-admin startproject session_tbd .       (session_tbd is the name of the project)
-Create account_app:
	Python manage.py startapp accounts_app
-Create profile_app:
	Python manage.py startapp profile_app
-Adjust project settings.py:
Add rest_framework, corsheaders, profile_app and accounts_app to INSTALLED_APPS
-Add 'corsheaders.middleware.CorsMiddleware', to MIDDLEWARE
-Add build to DIRS:
	os.path.join(BASE_DIR, ‘build’). 
	*Will give warning since frontend build is not complete.
-Adjust Database to postgresql and name to tbd_db
-Create database tbd_db
-Add STATICFILES_DIR = [ os.path.join(BASE_DIR, ‘build/static’) ]
	Will collect any additional static files
-Add STATIC_ROOT = os.path.join(BASE_DIR, ‘static’)
-Add 	REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.permissions.SessionAuthentication'
    ]
}
-Add CORS_ORIGIN_ALLOW_ALL = True
-Update Project urls.py
-Add urls.py file to account_app and profile_app
Create profile_app model and add one-to-one relationship with the Django Model User
Create views for accounts_app
Create urls for accounts_app
Create views for user_profile
Create urls for user_profile

