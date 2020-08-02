## legal-Wiz

### Task:
#### 1. Add all HTML pages in templates folder
#### 2. Add all CSS, JS and images inside static folder according to its type. Don't play with vendor folder there-in
#### 3. Username: legalwiz and password: shubham12345 for admin login
#### 4. Include folder path of templates and static inside settings.py at respective places
#### 5. To include files inside static folder, use syntax: {% static '' %} todo: place the path of the css/js/img inside ''
#### 6. Place the body of html inside {%block content%} {%endblock%} for all the pages. Include {% load static %} if u are using static files 
#### 7. Model creation: In models.py create class for the required thing and create variables accordingly. Then run these cmd in terminal.
  ##### - python manage.py makemigrations
  ##### - python manage.py migrate
#### 8. In urls.py create the urls of pages
#### 9. In views.py create methods of the defined url path
#### 10. For database:
##### - to add: objectname.objects.create(attribute = 'value',...)
##### - objectname.save()
