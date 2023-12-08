<template>
    <header style="border-radius: 1rem; ">
        <MenuComponent />
    </header>

    
    
    <div class="container-fluid p-0 box px-5" style="margin-top: 12vh; display: flex;">
        <div class="sidebar bg-light box-shadow-container me-4 box-rounded-container" style="height: 85vh;">
            <div class="container w-100 p-3">
                <nav>
                    <header>
                        <div class="logo">
                            <img src="https://cdn-icons-png.flaticon.com/512/12928/12928500.png" alt="logo image" style="width: 2.5vw;">
                            <h3 style="margin: auto 0;">My Library</h3>
                        </div>
                    </header><hr>
                    <ul class="list">
                        <li :class="{active: $route.path === '/'}"><RouterLink to="/">Started</RouterLink></li>
                        <li :class="{active: $route.path === '/intro'}"><RouterLink to="/intro" v-slot="{ route }">Introduction</RouterLink></li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="content bg-light w-100 box-shadow-container box-rounded-container py-3" style="height: 85vh; overflow-y: auto;">
            <div class="container w-100 p-3" style="overflow: hidden;">
                <RouterView v-slot="{Component}">
                    <Transition name="slide" mode="out-in">
                        <component :is="Component"></component>
                    </Transition>
                </RouterView>
            </div>
        </div>
    </div>

</template>
<script setup>
    import { ref, onMounted, watch } from 'vue';
    import SelectOptionWritterVue from './components/SelectOptionWritter.vue';
    import TestCompo from './components/TestCompo.vue';
    import MatchingOption from './components/MatchingOption.vue';
    import TestView from './views/TestView.vue';
    import axios from 'axios';
    import MenuComponent from './components/menuComponent.vue';
    import { Toast } from 'bootstrap';
    import 'bootstrap/dist/js/bootstrap';
    import 'bootstrap/dist/js/bootstrap.bundle';
    import SidebarComponent from './components/SidebarComponent.vue';
    import HeadaderComponent from './components/HeaderComponent.vue';
    import IntroductionView from './views/IntroductionView.vue';
    import { RouterLink } from 'vue-router';
    


</script>
<style scoped>
    body
    {
        background-image: url('https://images.pexels.com/photos/1261728/pexels-photo-1261728.jpeg');
    }

    /** translate */
    .slide-enter-active, .slide-leave-active
    {
        transition: opacity 0.5s, transform .8s;
    }

    .slide-enter-from, .slide-leave-to
    {
        opacity: 0;
        transform: translateX(-100%);
    }


    .sidebar
    {
        width: 400px;
    }

    .box-shadow-container
    {
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    }

    .box-rounded-container
    {
        border-radius: 1rem;
    }

    .logo
    {
        display: flex;
    }

    .list
    {
        margin: 0;
        padding: 0;
        /* list-style: none; */
        list-style-type: none;
    }

    .list li
    {
        display: block;
        list-style: none;
        list-style-type: none;
        border-radius: .5rem;
        margin-bottom: 0.2vh;
        border: 1px solid transparent;
    }
    
    .list li a
    {
        display: block;
        padding: 1vh;
    }

    .list li.active
    {
        background-color: #8a52fa;
        border: 1px solid #8244ff;
    }

    .list li:hover
    {
        background-color: #712cf9;
        border: 1px solid #6f27ff;
    }
    
    .list li.active a
    {
        color: #fff;
    }
    .list li:hover a
    {
        color: #fff;
    }
    
    .list li a
    {
        text-decoration: none;
    }
</style>