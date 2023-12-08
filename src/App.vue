<template>
    <header>
        <MenuComponent />
    </header>

    
    
    <div class="container-fluid p-0 box px-5" style="margin-top: 12vh; display: flex;">
        <div class="sidebar bg-light box-shadow-container me-4" style="height: 80vh;">
            a
        </div>
        <div class="content w-100 box-shadow-container box-rounded-container" style="height: 80vh;">
            <div class="container w-100">
                <RouterView />
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
    

    const txt = ref("Hello");
    

    
</script>
<style scoped>
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
</style>