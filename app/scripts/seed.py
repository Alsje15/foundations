from app.app import create_app
from app.routes.models import Recipe, Chef
from app.extensions.database import db

app = create_app()
app.app_context().push()

#&#10&#10 &#8226

recipes_data = {
    '1':{
        'image':'https://d2v9mhsiek5lbq.cloudfront.net/eyJidWNrZXQiOiJsb21hLW1lZGlhLXVrIiwia2V5IjoiZm9vZG5ldHdvcmstaW1hZ2UtNDY4YmNlMWMtMWZjNy00Njk1LWE5NzYtZTE5NWFmNjU3N2FiLmpwZyIsImVkaXRzIjp7InJlc2l6ZSI6eyJmaXQiOiJjb3ZlciIsIndpZHRoIjo4MTIsImhlaWdodCI6NDU3fSwianBlZyI6eyJxdWFsaXR5Ijo1NSwicHJvZ3Jlc3NpdmUiOnRydWV9fX0=', 
        'title':'Blue Cheese Steak Sandwich', 
        'category':5,
        'description':'A hearty soup perfect for a starter or a main with some quesadillas.',
        'instructions':'For 4 portions: \nCook 2 chopped onions in olive oil until tender and then add tomato paste. <br>Add 2 cans of tomatoes and vegetable broth - let it simmer for 3 minutes ... <br><br>Ingredients: <br>&#x2022 2 onions <br>&bull 5 tomatoes <br>&bull etc... ',
        'chef_id':2
    },
    '2':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'1 hour Lemon Pound Cake', 
        'category':2,
        'description':'An easy-peasy, fluffy, tangy lemon cake for any occasion.',
        'instructions':'For the cake, mix wet and dry ingredients seperately before combining. Pre-heat the oven at 180 degrees and then bake for 40 mins. \nFor the icing, mix ingredients in a bowl and leave in the fridge for at least 30 minutes. \n\nCake ingredients: \n500g flour \n50g sugar \n5 fresh lemons \nIcing ingredients: \n30g icing sugar \n100ml cold water',
        'chef_id':1
    },
    '3':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'The perfect pesto omelette', 
        'category':4,
        'description':'Sophisticated but easy omelettes for a hearty breakfast.',
        'instructions':'For each omelette: \nBreak 2 eggs into a bowl and mix with 15ml of water, some salt and pepper. On the side, chop up some cherry tomatoes, spinach, basil, and grate some cheese. \nWith a non-stick pan medium heated, add some butter and throw the mixed eggs in the pan. Once you see bubbles, add the fresh ingredients and cheese accross the surface of the omelette. After 3-5 minutes, dependent on preference, fold the omelette in half in the pan, cover the top with pesto and flip it and wait 1 minute. Repeat this with the other side.',
        'chef_id':3
    },
    '4':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'Therfect pesto omelette', 
        'category':4,
        'description':'Sophisticated but easy omelettes for a hearty breakfast.',
        'instructions':'For each omelette: \nBreak 2 eggs into a bowl and mix with 15ml of water, some salt and pepper. On the side, chop up some cherry tomatoes, spinach, basil, and grate some cheese. \nWith a non-stick pan medium heated, add some butter and throw the mixed eggs in the pan. Once you see bubbles, add the fresh ingredients and cheese accross the surface of the omelette. After 3-5 minutes, dependent on preference, fold the omelette in half in the pan, cover the top with pesto and flip it and wait 1 minute. Repeat this with the other side.',
        'chef_id':3
    },
    '5':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'The perfect p omelette', 
        'category':4,
        'description':'Sophisticated but easy omelettes for a hearty breakfast.',
        'instructions':'For each omelette: \nBreak 2 eggs into a bowl and mix with 15ml of water, some salt and pepper. On the side, chop up some cherry tomatoes, spinach, basil, and grate some cheese. \nWith a non-stick pan medium heated, add some butter and throw the mixed eggs in the pan. Once you see bubbles, add the fresh ingredients and cheese accross the surface of the omelette. After 3-5 minutes, dependent on preference, fold the omelette in half in the pan, cover the top with pesto and flip it and wait 1 minute. Repeat this with the other side.',
        'chef_id':3
    },
    '6':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'The perfect peto omelte', 
        'category':4,
        'description':'Sophisticated but easy omelettes for a hearty breakfast.',
        'instructions':'For each omelette: \nBreak 2 eggs into a bowl and mix with 15ml of water, some salt and pepper. On the side, chop up some cherry tomatoes, spinach, basil, and grate some cheese. \nWith a non-stick pan medium heated, add some butter and throw the mixed eggs in the pan. Once you see bubbles, add the fresh ingredients and cheese accross the surface of the omelette. After 3-5 minutes, dependent on preference, fold the omelette in half in the pan, cover the top with pesto and flip it and wait 1 minute. Repeat this with the other side.',
        'chef_id':3
    },
}

chef_data = {
    1:{
        'email':'scotty@gmail.com',
        'password':'scarn2022',
        'name':'Michael Scott',
        'image':'https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png',
        'description':'I am a professional baker with 22 years of experience.'
    },
    2:{
        'email':'jimmyjim@yahoo.com',
        'password':'noodles',
        'name':'Jimmy the Chef',
        'image':'https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png',
        'description':'I specialize in asian and vietnamese cooking.'
    },
    3:{
        'email':'lina55@gmail.com',
        'password':'cata55',
        'name':'Cooking Caterina',
        'image':'https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png',
        'description':'Reach out to me for your catering needs in Germany :)'
    },    
} 

# use to add
# for slug, recipe in recipes_data.items():
#     new_recipe = Recipe(slug=slug, image=recipe['image'], title=recipe['title'], category=recipe['category'], description=recipe['description'], instructions=recipe['instructions'], chef_id=recipe['chef_id'])
#     db.session.add(new_recipe)

# for id, chef in chef_data.items():
#     new_chef = Chef(id=id, email=chef['email'], password=chef['password'], name=chef['name'], image=chef['image'], description=chef['description'])
#     db.session.add(new_chef)

# use to delete
recipes = Recipe.query.all()
for recipe in recipes:
    recipe.delete()

chefs = Chef.query.all()
for chef in chefs:
    chef.delete()

db.session.commit()