#1. Cree el entorno virtual venv
#2. Cree .gitignore
#3. Cree README.md
#4. Cree requirements ()
    #django viene configurado para usar SQlite, entonces se instala en su lugar:
    #pip install mysqlclient
    #se instala mysqlclient para comunicar django con mysql
    #se instala django-environ para usar variables de entorno para ocultar contraseñas y configuraciones sensibles 
#5. Creación de archivo .env: archivo de texto plano para almacenar variables de configuración y credenciales de bd de forma segura(pares clave:valor)


#para crear un superusuario: python manage.py createsuperuser
#ejemplo:
# Username: matrona1
#Email address: matrona1@hospitalchillan.cl
#Password: Matrona2025*
#Password (again): Matrona2025*


#para cargar interfaz
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver

#para verificar migraciones aplicadas
#python manage.py showmigrations gestacion
#debe entregar: [X] 0001_initial


#PASO A PASO PARA ALGUIEN QUE LO CORRE POR PRIMERA VEZ
#python -m venv .venv
#source .venv/bin/activate
#pip install -r requirements.txt
#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver