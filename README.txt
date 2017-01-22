╔═════════════════════════════════════════════════════════════════════╗
║                   IRON LANTERN INSPECTIONS INC.	              ║ 
║	                                                              ║
║	             Walkthrough Assistance App                       ║
║	                                                              ║
║                 Jordan, Eric, Tam, Hakan, Windjy                    ║
╚═════════════════════════════════════════════════════════════════════╝

LANGUAGES
python 3.5 (check installed version | python --version)
django 1.10.4 (check installed version | python -c "import django; print(django.get_version())")
html 5.1
boostrap 3.3.7
jQuery 3.1.1
SASS 3.4.22

RUN SERVER
1. open Iron Lantern app folder
2. shift + right-click >> Open command window here
3. python manage.py runserver
4. open browser with provided IP address in command line
5. example http://127.0.0.1:8000/inspection/, http://127.0.0.1:8000/admin/ 

FOLDER TREE
+ .vscode    // FOLDER DESCRIPTION - ? // 
    - launch.json :    // FILE DESCRIPTION - ? //
    - settings.json :    // FILE DESCRIPTION - ? //                    
+ home_inspection : app for inspection   
    +pycache : auto generated  
    +migrations : auto generated
    +static : contains js, css, images for app 
    +templates 
        - index.html : homepage content    // TO MOVE INTO INSPECTION DIRECTORY
	+ inspection 
	    - about.html : about content
	    - articles.html : technical articles content
	    - base.html : repeating layout on everypage
            -component.html : content for component page
	    - contact.html : contact content
	    - dashboard : user dashboard to start report, review reports, edit profile, logout
	    - inspector_rooms.html : inspector report room selection //CAN IT BE ALTERED TO TO BE USED FOR ALL TYPES OF REPORTS?
	    - inspector_start.html : inspector start new report //CAN IT BE ALTERED TO TO BE USED FOR ALL TYPES OF REPORTS?
	    - login.html : user login page, registration redirect
	    - profile.html : edit profile page
	    - register.html : new user registration  
            -room.html : content for room   
	    - terms.html : terms and conditions content
	    - user_reports.html : standalone user reports page
    +uploads : images that user upload should goes here      // TO DO //   
    -__init.py : load needed packages, empty right now    	
    - admin.py : if create a new model, goes here and add name of that model to array so you can see it in admin page    
    - apps.py : haven't touch    
    - forms.py : group DB values to create form models    
    - models.py : DB data blueprint    
	NOTE: if you change the structure of any model, need to open new command line & run 'python manage.py makemigrations home_inspection' & 'python manage.py migrate'	
    - service.py :    // FILE DESCRIPTION - ? //
    - urls.py : define url query patterns
    - views.py : retrieve data from database and send it to your templates (eg controller) 
+ IAWD    // FOLDER DESCRIPTION - ? //            
- changelog.txt : track changes // TO UPDATE
- db.sqlite3 : app database
- manage.py : django management system
- README.txt
