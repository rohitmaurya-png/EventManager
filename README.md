# EventManager
This website was made while learing django framework. 

A event Management website in python + Django with bulma css framework

Dependency
Django-```pip install django```
Django is a high-level Python Web framework

Stripe-```pip install stripe```
Stripe - A complete payments platform

Pillow-```pip install pillow```
Pillow is a Python Imaging Library
(dose not support png if used will throw a os error)

To Run this Project use the following command


1.```python -m venv env```
creates virtual enviroment

2.```python manage.py makemigrations```
generates the SQL commands for preinstalled app

3.```python manage.py migrate```
migrate executes those SQL commands in the database file

3.```Python manage.py migrate --run-syncdb```
reconstruct database schema according to altered model fields(not necessary)

4.```python manage.py createsuperuser```
It will create an admin superuser with all Administrative privileges

5.```python manage.py runserver```
runs the server on localhost.
127.0.0.1:8000



Home page
![Home Page](./screenshot/Welcome_Event.png)

become Co-ordinator- can manage his events/orders/view other co-ordinators
![Become Co-ordinator](./screenshot/Become_coordinator_Event.png)


Add event page
![Add event page](./screenshot/Add_event_Event.png)

Superuserlogin 
url= 127.0.0.1:8000/admin
![Superuser login](./screenshot/Log_in_Welcome_To_Staff_Co-ordinator_Dashboard.png)

Superuser admin panel(django-admin)
![Superuser admin panel](./screenshot/Welcome_To_Staff_Co-ordinator_Dashboard_Welcome_To_Staff_Co-ordinator_Dashboard.png)

Co-ordinator Admin Panel
![Co-ordinator Admin Panel](./screenshot/Coordinator_admin_Event.png)
