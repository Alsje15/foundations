from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object('app.config')

# static routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signin')
def singin():
    return render_template('signin.html')

@app.route('/addrecipe')
def addrecipe():
    return render_template('addrecipe.html')

# dynamic routes
slug = 349

@app.route('/recipe/<slug>')
def recipe(slug):
    return render_template('recipe.html', slug=slug)

# Initialise db
# def register_extensions(app:Flask):
#     db.init__app(app)
#     migrate.init__app(app, db)
