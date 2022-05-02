# NAME
Cheffing : A blog for professional freelancer chefs in Germany to share recipes with the public and gain exposure.

# DESCRIPTION
www.cheffing.de consists of a HOME(index), RECIPE(index/<slug>) ABOUT and SIGN IN page that is database dependent. With authorization approved authors/chefs can access the ADD RECIPE page. All pages are also dependent on base.html.

Useability for chefs: 
    They must apply to join the community by emailing the Cheffing owner. If approved they are manually added to the SQLite database, will receive a password and can SIGN IN. They can then edit their profile on the ABOUT page and add their recipes on the HOME page.

Useability for users:
    In search of recipes the user can browse and filter through Our Recipes on the HOME page and press on one to view it in detail. Details include title, description, category, an image, recipe instructions and the author.
    In search to hire a chef the user can browse through Our Chefs on the ABOUT page. Details include their picture, name, bio and contact details.

# VISUALS
![logo](https://user-images.githubusercontent.com/101812067/166206010-947638c9-7a1f-48b6-bea0-62d2c1cef1d0.png)
![logo-sml](https://user-images.githubusercontent.com/101812067/166206012-eeb54731-e5ca-4978-b83a-ce624e0dc2ab.png)
![logo-sml2](https://user-images.githubusercontent.com/101812067/166206014-b10bbbdb-fee9-4943-ba2a-0ef839e0958b.png)
![icon-ig](https://user-images.githubusercontent.com/101812067/166206002-5d258966-924d-4b77-afa9-77a26a7e5379.png)
![icon-li](https://user-images.githubusercontent.com/101812067/166206005-377a4285-023e-4f16-8e78-7401086d9be5.png)
![icon-pi](https://user-images.githubusercontent.com/101812067/166206006-f96806c8-4036-439a-9a81-58734ea52583.png)
![icon-fb](https://user-images.githubusercontent.com/101812067/166206015-85c5ec59-f2c1-4f6a-a1ea-c20ed3423474.png)

# INSTALLATION AND USAGE
![Web Architecture](https://user-images.githubusercontent.com/101812067/166204539-5750b6ac-b0da-43ff-ab33-64958e33de01.jpg)
    
The project comes with seed data and a few basic tests. To sign in use one of the sign in details (email and password) found in chefs_data in seed.py, eg:
    email: scotty@gmail.com
    password: scarn2022
    
To test it locally instead of deployed on Heroku,
replace line 7 in config.py with:
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    
    Also create a virtual environment and add the following to your .env file:
    FLASK_ENV=development
    FLASK_APP=run.py
    DATABASE_URL=sqlite:///your_database.db
    SECRET_KEY=your_secret_key

# REQUIREMENTS
Copied from requirements.txt:
alembic==1.7.7
atomicwrites==1.4.0
attrs==21.4.0
click==8.1.2
colorama==0.4.4
distlib==0.3.4
filelock==3.6.0
Flask==2.1.1
Flask-Login==0.6.0
Flask-Migrate==3.1.0
Flask-SQLAlchemy==2.5.1
greenlet==1.1.2
gunicorn==20.1.0
iniconfig==1.1.1
itsdangerous==2.1.2
Jinja2==3.1.1
Mako==1.2.0
MarkupSafe==2.1.1
migrate==0.3.7
packaging==21.3
Pillow==8.4.0
platformdirs==2.5.1
pluggy==1.0.0
psycopg2==2.9.3
py==1.11.0
pyparsing==3.0.8
pytest==7.1.1
python-dotenv==0.19.2
six==1.16.0
SQLAlchemy==1.4.35
tomli==2.0.1
virtualenv==20.13.3
Werkzeug==2.1.1
    
# AUTHORS AND ACKNOWLEDGEMENT
Author, designer and developer: Alsje Lourens

# SUPPORT
Contact the developer at alsje.lourens@code.berlin

# LICENSE
None

# PROJECT STATUS
Everything is complete except for the upload and display of local images: there are temporary fields that just take links (recipe image and author/chef image). Another lacking feature is for the author/chef to change their password after initial sign in.
