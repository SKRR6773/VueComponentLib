import { createRouter, createWebHashHistory } from "vue-router";

import Home from '../views/Home.vue';
import Test from '../views/TestView.vue';
import Introduction from '../views/IntroductionView.vue';



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
            component: Introduction
        },
        {
            path: "/test/:id",
            name: "Test",
            component: Test
        }
    ]
});


 
export default router;