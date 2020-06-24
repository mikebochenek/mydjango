# mydjango - My Data Visualization project!
The idea is to make Visualization dummy-proof -beyond-Excel (TM)

# dependencies
	sudo apt-get install python-pip apache2 libapache2-mod-wsgi
	sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
	sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
	sudo a2enmod wsgi

	sudo pip install virtualenv
	source mydjangoenv/bin/activate

	pip install django psycopg2
	pip install streamlit


# manage commands
	manage.py collectstatic 
	manage.py runserver
	manage.py migrate
	manage.py makemigrations
	manage.py createsuperuser  
