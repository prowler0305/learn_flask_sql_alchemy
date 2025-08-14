import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {path: '/students', component: () => import('./components/student_table.vue')},
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;