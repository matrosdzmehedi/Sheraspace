# Sheraspace

#First create virtual environment, then install dependencies

pip install -r requirements.txt 

#Migrate database

python manage.py migrate

python manage.py makemigrations cv

python manage.py migrate



#Createsuperuser

python manage.py createsuperuser


#Runserver

python manage.py runserver




