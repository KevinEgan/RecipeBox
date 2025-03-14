<template>
  <div class="app">
    <header>
      <h1>Recipe Sharing App</h1>
    </header>
   
    <main>
      <div class="recipe-form">
        <h2>Add New Recipe</h2>
        <form @submit.prevent="addRecipe">
          <div class="form-group">
            <label>Title:</label>
            <input v-model="newRecipe.title" required>
          </div>
          <div class="form-group">
            <label>Ingredients:</label>
            <textarea v-model="newRecipe.ingredients" required></textarea>
          </div>
          <div class="form-group">
            <label>Instructions:</label>
            <textarea v-model="newRecipe.instructions" required></textarea>
          </div>
          <div class="form-group">
            <label>Cooking Time:</label>
            <input v-model="newRecipe.cooking_time">
          </div>
          <div class="form-group">
            <label>Difficulty:</label>
            <input type="number" v-model="newRecipe.difficulty">
          </div>
          <div class="form-group">
            <label>Rating:</label>
            <input type="number" v-model="newRecipe.stars_rating">
          </div>
          <button type="submit">Add Recipe</button>
        </form>
      </div>

      <div class="recipe-list">
        <h2>Recipes</h2>
        <div v-for="recipe in recipes" :key="recipe.id" class="recipe-card">
          <h3>{{ recipe.title }}</h3>
          <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>
          <p><strong>Instructions:</strong> {{ recipe.instructions }}</p>
          <p v-if="recipe.cooking_time"><strong>Cooking Time:</strong> {{ recipe.cooking_time }}</p>
          <p v-if="recipe.difficulty"><strong>Difficulty:</strong> {{ recipe.difficulty }}</p>
          <p v-if="recipe.stars_rating"><strong>Rating:</strong> {{ recipe.stars_rating }}</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      recipes: [],
      newRecipe: {
        title: '',
        ingredients: '',
        instructions: '',
        cooking_time: '',
        servings: null
      }
    }
  },
  methods: {
    async fetchRecipes() {
      try {
        const response = await axios.get('http://localhost:5000/api/recipes');
        this.recipes = response.data;
      } catch (error) {
        console.error('Error fetching recipes:', error);
      }
    },
    async addRecipe() {
      try {
        const response = await axios.post('http://localhost:5000/api/recipes', this.newRecipe);
        this.recipes.push(response.data);
        this.newRecipe = {
          title: '',
          ingredients: '',
          instructions: '',
          cooking_time: '',
          difficulty: null,
          stars_rating:null
        };
      } catch (error) {
        console.error('Error adding recipe:', error);
      }
    }
  },
  mounted() {
    this.fetchRecipes();
  }
}
</script>

<style>
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  text-align: center;
  margin-bottom: 40px;
}

.recipe-form {
  max-width: 600px;
  margin: 0 auto 40px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

textarea {
  height: 100px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.recipe-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.recipe-card {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.recipe-card h3 {
  margin-top: 0;
  color: #333;
}
</style> 