from flask import current_app
# Example:
from app.py import Recipe

recipes_data = [
    {
        "title": "Ham Sandwich",
        "ingredients": "Ham, Bread",
        "instructions": "Put ham between two slices of bread\nEnjoy!",
        "cooking_time": "4 hours",
        "difficulty": 10,
        "star_rating": 5
    }
]

def upgrade():
    #get recipe table
    meta = MetaData()
    recipe_table = Table('recipe', meta)

    #insert recipes
    op.bulk_insert(
        recipe_table,
        recipes_data
    )

def downgrade():
    op.execute('DELETE FROM recipe WHERE title IN ({})'.format(
        '.'.join([f"'{recipe['title']}" for recipe in recipes_data])
    ))


# initial_user = {


#     'username': 'superadmin'
# }
# if User.find_by_username(initial_user['username']) is None:
#     User(**initial_user).save()
