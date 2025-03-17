from app import db, Recipe
from wsgi import app

def seed_database():
    recipes = [
        {
            'title': 'Ham Sandwich',
            'ingredients': 'Bread, Ham',
            'instructions':'Put ham between two slices of bread. \nEnjoy!',
            'cooking_time': '4 Hours',
            'difficulty': 5,
            'stars_rating': 5
        }
    ]

    with app.app_context():
        db.create_all()

        for recipe_data in recipes:
            recipe = Recipe(**recipe_data)
            db.session.add(recipe)

        db.session.commit()
        print("Database seeded")

if __name__=='__main__':
    seed_db()