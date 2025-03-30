<template>
    <div class="add-recipe">
      <header>
        <h1>Add New Recipe</h1>
        <router-link to="/" class="back-button">Back to Recipes</router-link>
      </header>
     
      <div class="recipe-form">
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
            <input type="number" v-model="newRecipe.cooking_time">
          </div>
          <div class="form-group">
            <label>Difficulty:</label>
            <input type="number" v-model="newRecipe.difficulty">
          </div>
          <div class="form-group">
            <label>Stars:</label>
            <input type="number" v-model="newRecipe.stars_rating">
          </div>
          <button type="submit">Add Recipe</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AddRecipeView',
    data() {
      return {
        newRecipe: {
          title: '',
          ingredients: '',
          instructions: '',
          cooking_time: 0,
          difficulty: 0,
          stars_rating: 0
        }
      }
    },
    methods: {
      async addRecipe() {
        try {
          console.log('Sending recipe:', this.newRecipe);
          await axios.post('http://localhost:5000/api/recipes', this.newRecipe);
          console.log('Recipe sent successfully!')
          this.$router.push('/'); // Redirect to home page
        } catch (error) {
          console.error('Error adding recipe:', error);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .add-recipe {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40px;
  }
  
  .back-button {
    background-color: #666;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 4px;
  }
  
  .back-button:hover {
    background-color: #555;
  }
  
  .recipe-form {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #ddd;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
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
  </style>
  