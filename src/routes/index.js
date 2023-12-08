import { createRouter, createWebHashHistory } from "vue-router";

import Home from '../views/Home.vue';
import Test from '../views/TestView.vue';
import Introduction



const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: "/",
            name: "Home",
            component: Home
        },
        {
            path: "/intro",
            name: "Introduction",
            component: 
        },
        {
            path: "/test/:id",
            name: "Test",
            component: Test
        }
    ]
});


 
export default router;