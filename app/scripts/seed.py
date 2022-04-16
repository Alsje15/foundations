from app.app import create_app
from app.routes.models import Recipe, Chef
from app.extensions.database import db

app = create_app()
app.app_context().push()

recipes_data = {
    'tomato-soup':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'Creamy Tomato Soup', 
        'category':'3',
        'description':'A hearty soup perfect for a starter or a main with some quesadillas.',
        'instructions':'For 4 portions: \nCook 2 chopped onions in olive oil until tender and then add tomato paste. \nAdd 2 cans of tomatoes and vegetable broth - let it simmer for 3 minutes ... \n\nIngredients: \n- 2 onions \n- 5 tomatoes \n- etc... ',
        'chef_id':'2'
    },
    'lemon-cake':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'1 hour Lemon Pound Cake', 
        'category':'2',
        'description':'An easy-peasy, fluffy, tangy lemon cake for any occasion.',
        'instructions':'For the cake, mix wet and dry ingredients seperately before combining. Pre-heat the oven at 180 degrees and then bake for 40 mins. \nFor the icing, mix ingredients in a bowl and leave in the fridge for at least 30 minutes. \n\nCake ingredients: \n500g flour \n50g sugar \n5 fresh lemons \nIcing ingredients: \n30g icing sugar \n100ml cold water',
        'chef_id':'1'
    },
    'pesto-omelette':{
        'image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxKcB2P30aFTTgtHsokrfFFKQkW7ndLTbM0Q&usqp=CAU', 
        'title':'The perfect pesto omelette', 
        'category':'4',
        'description':'Sophisticated but easy omelettes for a hearty breakfast.',
        'instructions':'For each omelette: \nBreak 2 eggs into a bowl and mix with 15ml of water, some salt and pepper. On the side, chop up some cherry tomatoes, spinach, basil, and grate some cheese. \nWith a non-stick pan medium heated, add some butter and throw the mixed eggs in the pan. Once you see bubbles, add the fresh ingredients and cheese accross the surface of the omelette. After 3-5 minutes, dependent on preference, fold the omelette in half in the pan, cover the top with pesto and flip it and wait 1 minute. Repeat this with the other side.',
        'chef_id':'3'
    },
}

chef_data = {
    'michael-scott':{
        'email':'',
        'password':'',
        'name':'',
        'image':'',
        'description':''
    },
    'michael-scott':{
        'email':'',
        'password':'',
        'name':'',
        'image':'',
        'description':''
    },    
    'michael-scott':{
        'email':'',
        'password':'',
        'name':'',
        'image':'',
        'description':''
    },    
}