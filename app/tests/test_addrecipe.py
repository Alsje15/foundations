from app.routes.models import Recipe
    
def test_addrecipe_post(client):
    response = client.post('/addrecipe', data={
        'slug':'fried-egg',
        'image':'https://cookieandkate.com/images/2018/09/crispy-fried-egg-recipe.jpg',
        'title':'Fried Egg',
        'category':1,
        'description':'Lorem Ipsum',
        'instructions':'Lorem Ipsum',
        'chef_id':1
    })
    assert Recipe.query.first() is not None