import { createRouter, createWebHashHistory } from "vue-router";

import Home from '../views/Home.vue';
import Test from '../views/TestView.vue';



const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: "/",
            name: "Home",
            component: Home
        },
        {
            path: "/test/:id",
            name: "Test",
            component: Test
        }
    ]
});



export default router;