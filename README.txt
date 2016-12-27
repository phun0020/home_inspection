╔═════════════════════════════════════════════════════════════════════╗
║                   IRON LANTERN INSPECTIONS INC.	                    ║ 
║	                                                                    ║
║	                   Walkthrough Assistance App                       ║
║	                                                                    ║
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
+.vscode      // FOLDER DESCRIPTION - ? //                        // @TAM: WHATS THE JSON FOR?//
+IAWD      // FOLDER DESCRIPTION - ? //                                
+home_inspection : app for inspection   
	+pycache : auto generate when run   
	+migrations : auto generate                               // @TAM: AUTO GENERATE WHAT? FIELD INFORMAITON? //
	+static : contains js, css, images for app                // @TAM: WHY HAVE SUBFOLDER 'INSPECTION' WHEN STATIC IS SUB OF HOME_INSPECTION? INSPECTION = VIEW?//
	+templates                                                // @TAM: WHY HAVE SUBFOLDER 'INSPECTION' WHEN TEMPLATES IS SUB OF HOME_INSPECTION? INSPECTION = VIEW?//
	
	   -base.html : layout for everypage such as header, footer // ONGOING INTEGRATION - ERIC //
	   
	   -component.html : content for component page       
	   -index.html : content for homepage       
	   -room.html : content for room   
	+uploads : images that user upload should goes here      // TO DO - TAM //   
	-__init.py : load needed packages, empty right now    
	
 (?)-admin.py : if create a new model, goes here and add name of that model to array so you can see it in admin page    
 (?)-apps.py : haven't touch    
 (?)-test.py : your test cases go here  


	-forms.py : group DB values to create form models    
	-models.py : DB data blueprint    
		NOTE: if you change the structure of any model, need to open new command line & run 'python manage.py makemigrations home_inspection' & 'python manage.py migrate'	
	-urls.py : define url query patterns, ???? connect with urls.py in parent folder    ????
	-views.py : retrieve data from database and send it to your templates (eg controller) 
-changelog.txt :      // FILE DESCRIPTION - ? //
-db.sqlite3 : app database
-manage.py :      // FILE DESCRIPTION - ? //
-README.txt
