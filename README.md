Eric, Hakan, Windjy, Tam
packages:
- python 3.5 (to check your version | python --version)
- django 1.10.4 (to check your version | python -c "import django; print(django.get_version())")
to run:
1. go to IAWD folder
2. shift + right-click >> Open command window here
3. python manage.py runserver
4. open browser with provided IP address in command line
5. example http://127.0.0.1:8000/inspection/, http://127.0.0.1:8000/admin/
IAWD
   +home_inspection : app for inspection
    +__pycache__ : auto generate when run
    +migrations : auto generate
    +static : contains js, css, images for app
    +templates
       -base.html : layout for everypage such as header, footer
       -component.html : content for component page
       -index.html : content for property page
       -room.html : content for room
    +uploads : images that user upload should goes here (haven't implement)
    +__init.py : load needed packages, empty right now
    +admin.py : if create a new model, goes here and add name of that model to array so you can see it in admin page
    +apps.py : haven't touch
    +forms.py : save form models which are used when working with form
    +models.py : where you save all your models, just like blueprint to your database
    NOTE: if you change the structure of any model, need to open new command line, python manage.py makemigrations home_inspection && python manage.py migrate
    +test.py : your test cases go here
    +urls.py : route for you app, connect with urls.py in parent folder
    +views.py : kinda likes controller, retrieve data from database and send it to your templates
    
    Everything follows the tutorial on codeschool
