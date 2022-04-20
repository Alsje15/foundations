from app.routes.models import Recipe

def test_index_success(client):
    response = client.get('/')
    assert response.status_code == 200

def test_recipes_render(client):
    # Arrange
    new_recipe = Recipe(slug='fried-egg', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', title='Fried Egg', category=1, description='A fried egg.', instructions='Break egg in pan.', chef_id=1)
    new_recipe.save()

    # Act
    response = client.get('/')

    # Assess
    assert b'Fried Egg' in response.data