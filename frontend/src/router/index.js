import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddRecipeView from '../views/AddRecipeView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/add-recipe',
            name: 'add-recipe',
            component: AddRecipeView
        }
    ]

})

export default router