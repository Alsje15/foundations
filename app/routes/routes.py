from flask import Blueprint, render_template, redirect, request, current_app
from flask_login import login_required, login_user, logout_user, current_user
from .models import Recipe, Chef
from slugify import slugify

blueprint = Blueprint('routes',__name__)

@blueprint.route('/')
def index():
    page_number = request.args.get('page', 1, type=int)
    chefs = Chef.query.all()
    recipes_pagination = Recipe.query.paginate(page_number, current_app.config['RECIPES_PER_PAGE'])
    return render_template('index.html', recipes_pagination=recipes_pagination, chefs=chefs)

@blueprint.route('/category/<category>')
def filter(category):
    page_number = request.args.get('page', 1, type=int)
    chefs = Chef.query.all()
    recipes_pagination = Recipe.query.filter_by(category=category).paginate(page_number, current_app.config['RECIPES_PER_PAGE'])
    return render_template('index.html', recipes_pagination=recipes_pagination, chefs=chefs)


@blueprint.route('/recipe/<slug>')
def recipe(slug):
    recipe = Recipe.query.filter_by(slug=slug).first_or_404()
    return render_template('recipe.html', recipe=recipe)


@blueprint.get('/about')
def about():
    page_number = request.args.get('page', type=int)
    chefs_pagination = Chef.query.paginate(page_number, current_app.config['CHEFS_PER_PAGE'])
    return render_template('about.html', chefs_pagination=chefs_pagination)

@blueprint.post('/about')
def updatechef():    

    chef = Chef.query.filter_by(id=current_user.get_id()).first_or_404()

    chef.delete()

    chef = Chef(
        id=current_user.get_id(),
        email=request.form.get('email'),
        password=chef.password,
        name=request.form.get('name'),
        image=request.form.get('image'),        
        description=request.form.get('description'),
    )

    chef.save()
    return redirect('/about')


@blueprint.get('/signin')
def signin_get():
    return render_template('signin.html')

@blueprint.post('/signin')
def signin_post():
    try:
        user = Chef.query.filter_by(email=request.form.get('email'), password=request.form.get('password')).first()

        if not user:
            raise Exception('Incorrect sign in details. Please try again.')

        login_user(user)
        return redirect('/')

    except Exception as error_message:
        error = error_message or 'An error occured while logging in. Please report this error to Cheffing if you are already a Cheffing member.'
        return render_template('signin.html', error=error)
    

@blueprint.get('/signout')
def signout():
    logout_user()
    return redirect('/')


@blueprint.get('/addrecipe')
@login_required
def addrecipe_get():
    recipe = Recipe.query.all()
    return render_template('addrecipe.html', recipe=recipe)

@blueprint.post('/addrecipe')
def addrecipe_post():
    recipe = Recipe.query.all()

    recipe = Recipe(
        slug=slugify(request.form.get('title', '')),
        image=request.form.get('image'),
        title=request.form.get('title'),
        category=request.form.get('category'),
        description=request.form.get('description'),
        instructions=request.form.get('instructions'),
        chef_id=current_user.get_id()
    )

    if not all([
        request.form.get('title'),
        request.form.get('description'),
        request.form.get('instructions'),
    ]):
        return render_template('addrecipe.html', recipe=recipe, error='Please fill out all fields.')
        
    recipe.save()
    return redirect('/')


@blueprint.route('/removerecipe/<id>')
def removerecipe(id):    

    recipe = Recipe.query.filter_by(id=id).first_or_404()
    recipe.delete()

    return redirect('/')
