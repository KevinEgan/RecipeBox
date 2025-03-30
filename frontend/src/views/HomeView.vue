<template>
    <div class="home">
      <header>
        <h1>Recipe Collection</h1>
        <router-link to="/add-recipe" class="add-button">Add New Recipe</router-link>
      </header>
     
      <div class="recipe-list">
        <div v-for="recipe in recipes" :key="recipe.id" class="recipe-card">
          <h3>{{ recipe.title }}</h3>
          <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>
          <p><strong>Instructions:</strong> {{ recipe.instructions }}</p>
          <p v-if="recipe.cooking_time"><strong>Cooking Time:</strong> {{ recipe.cooking_time }}</p>
          <p v-if="recipe.difficulty"><strong>Difficulty:</strong> {{ recipe.difficulty }}</p>
          <p v-if="recipe.star_rating"><strong>Stars:</strong> {{ recipe.star_rating }}</p>

        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'HomeView',
    data() {
      return {
        recipes: []
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
      }
    },
    mounted() {
      this.fetchRecipes();
    }
  }
  </script>
  
  <style scoped>
  .home {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 40px;
  }
  
  .add-button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 4px;
  }
  
  .add-button:hover {
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