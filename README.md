# mydjango - My Data Visualization project!
- The idea is to make Visualization dummy-proof -beyond-Excel (TM)
- It would be cool to guess how to draw the data (based on some clever algorithms, tweaked with ML!)

## libraries to use
Library | Notes or comments
--- | --- 
[Altair](https://github.com/altair-viz/altair) | interactive graphs
[D Tale](https://pypi.org/project/dtale/) | interactive graphs
[Various libaries](https://beepb00p.xyz/hpi.html) | "Human Programming Interface"
[Streamlit.io](https://www.streamlit.io/) | the fastest way to build data apps

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
