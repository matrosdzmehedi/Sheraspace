# Sheraspace

#First create virtual environment using pip or venv or pipenv(i have used pipenv)

#i am using python version=3.8.5(use python =>3.5 )


#then install dependencies

pip install -r requirements.txt 

#Migrate database

python manage.py migrate

python manage.py makemigrations cv

python manage.py migrate



#Createsuperuser

python manage.py createsuperuser


#Runserver

python manage.py runserver




