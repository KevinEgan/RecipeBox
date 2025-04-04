from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
#from . import db, migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    CORS(app)

    #SQLite database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
   #db = SQLAlchemy(app)
   #migrate = Migrate(app, db)

    #Recipe Model
    class Recipe(db.Model):
        __tablename__ = 'recipes'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(150), nullable=False)
        ingredients = db.Column(db.Text, nullable=False)
        instructions = db.Column(db.Text, nullable=False)
        cooking_time = db.Column(db.String(50))
        difficulty = db.Column(db.Integer)
        stars_rating = db.Column(db.Integer)
        #A quirk of SQLite is that it doesn't deal with decimals, it will be treated as a String...
        #Which maybe is good enough for what I want to achieve (star rating). I will need to come back to this
        
        def to_dict(self):
            return{
                'id': self.id,
                'title': self.title,
                'ingredients': self.ingredients,
                'instructions': self.instructions,
                'cooking_time': self.cooking_time,
                'difficulty': self.difficulty,
                'stars_rating': self.stars_rating
            }
        
    #create tables
    with app.app_context():
        db.create_all()

    # Routes
    @app.route('/api/recipes', methods=['GET'])
    def get_recipes():
        #SQLite's version of SELECT * FROM recipe;
        recipes = Recipe.query.all()
        return jsonify([recipe.to_dict() for recipe in recipes])
    
    @app.route('/debug/schema')
    def debug_schema():
        with app.app_context():
            result = db.session.execute("PRAGMA table_info(recipe)")
            columns = result.fetchall()
            return jsonify([{
                'name':col[1],
                'type':col[2],
                'notnull':col[3]
            }for col in columns])

    @app.route('/debug/db')
    def debug_db():
        try:
            # Try to query the database
            result = db.session.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = result.fetchall()
            return jsonify({
                'status': 'connected',
                'tables': [table[0] for table in tables]
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'error': str(e)
            })

    @app.route('/api/recipes', methods=['POST'])
    def create_recipe():
        data = request.json
        print("Recieved data: ", data)
        new_recipe = Recipe(
            title=data['title'],
            ingredients=data['ingredients'],
            instructions=data['instructions'],
            cooking_time=data['cooking_time'],
            #get returns none if missing
            difficulty=data.get('difficulty'),
            stars_rating=data.get('stars_rating'),
        )
        print("Recipe before save (instructions):", new_recipe.instructions)
        db.session.add(new_recipe) # stages the recipe for saving
        db.session.commit() # saves recipe to database
        print("RECIPE SAVED!!")
        return jsonify(new_recipe.to_dict()), 201

    @app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
    def get_recipe(recipe_id):
        recipe = Recipe.query.get_or_400(recipe_id)
        return jsonify(recipe.to_dict())
    
    return app

    

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
