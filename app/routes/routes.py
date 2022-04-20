from flask import Blueprint, render_template, redirect, url_for, request, current_app
from .models import Recipe, Chef

blueprint = Blueprint('routes',__name__)

@blueprint.route('/')
def index():
    page_number = request.args.get('page', 1, type=int)
    #category = request.args.get('filter_by', 1, type=int)
    recipes_pagination = Recipe.query.paginate(page_number, current_app.config['RECIPES_PER_PAGE'])
    return render_template('index.html', recipes_pagination=recipes_pagination)

@blueprint.route('/<slug>')
def recipe(slug):
    recipe = Recipe.query.filter_by(slug=slug).first_or_404()
    return render_template('recipe.html', recipe=recipe)

@blueprint.route('/about')
def about():
    page_number = request.args.get('page', type=int)
    chefs_pagination = Chef.query.paginate(page_number, current_app.config['CHEFS_PER_PAGE'])
    return render_template('about.html', chefs_pagination=chefs_pagination)

@blueprint.route('/signin')
def singin():
    return render_template('signin.html')

@blueprint.route('/sign-in')
def sign_in():
    return redirect(url_for('signin.html'))

@blueprint.get('/addrecipe')
def addrecipe_get():
    recipe = Recipe.query.all()
    return render_template('addrecipe.html', recipe=recipe)

@blueprint.post('/addrecipe')
def addrecipe_post():
    recipe = Recipe.query.all()

    recipe = Recipe(
        # generate slug and get id?
        slug=request.form.get('slug'),
        image=request.form.get('image'),
        title=request.form.get('title'),
        category=request.form.get('category'),
        description=request.form.get('description'),
        instructions=request.form.get('instructions'),
        chef_id=request.form.get('chef_id')
    )

    if not all([
        request.form.get('title'),
        request.form.get('description'),
        request.form.get('instructions'),
    ]):
        return render_template('addrecipe.html', recipe=recipe, error='Please fill out all fields.')
        
    recipe.save()

    # Does this work? Going back to index when saved
    # How to edit if yours? Same with about
    return render_template('index.html', recipe=recipe)