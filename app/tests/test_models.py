from app.extensions.database import db
from app.routes.models import Recipe

def test_recipe_update(client):
    # Arrange
    recipe = Recipe(slug='fried-egg', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', title='Fried Egg', category=1, description='A fried egg.', instructions='Break egg in pan.', chef_id=1)
    db.session.add(recipe)
    db.session.commit()

    # Act
    recipe.title = 'Noodles'
    recipe.save()

    # Assess
    updated_recipe = Recipe.query.filter_by(slug='fried-egg').first()
    assert updated_recipe.title == 'Noodles'

def test_recipe_delete(client):
    # Arrange
    recipe = Recipe(slug='fried-egg', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', title='Fried Egg', category=1, description='A fried egg.', instructions='Break egg in pan.', chef_id=1)
    db.session.add(recipe)
    db.session.commit()

    # Act
    recipe.delete()

    # Assess
    deleted_recipe = Recipe.query.filter_by(slug='fried-egg').first()
    assert deleted_recipe is None