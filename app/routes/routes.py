from flask import Blueprint, render_template, redirect, url_for
from .models import Recipe, Chef

recipes_data = {
    'tomato-soup':{'name':'Tomato Soup', 'category':'1'},
    'lemon-cake':{'name':'Lemon Cake', 'category':'2'},
}

blueprint = Blueprint('routes',__name__)

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/about')
def about():
    return render_template('about.html')

@blueprint.route('/signin')
def singin():
    return render_template('signin.html')

@blueprint.route('/sign-in')
def sign_in():
    return redirect(url_for('signin.html'))

@blueprint.route('/addrecipe')
def addrecipe():
    return render_template('addrecipe.html')

@blueprint.route('/recipe/<slug>')
def recipe(slug):
    if slug in recipes_data:
        return render_template('recipe.html', recipe=recipes_data[slug]['name'])
        # return '<h1>' + recipes_data[slug]['name'] + '</h1>'
    else:
        return 'Sorry that recipe does not exist.'

# @blueprint.route('/recipe')
# def recipe():
#     return render_template('recipe.html', recipe=recipes_data)