<template>
    <header>
        <MenuComponent />
    </header>

    {{ <> ... <> }} <div></div> #in
    
    <RouterView />
    
    <div class="container p-0 box" style="margin-top: 10vh;">
        <div class="container-fluid bg-light" style="box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;">
            
            <div>
                <span>
                    {{ __txt__ }}
                </span>
            </div>
            <!-- header sidebar and menu -->
            
            <section class="content" style="overflow: hidden;">
                <!-- content -->
                
                <div class="container">
                    <RouterLink to="/test/a">a</RouterLink>
                </div>

            </section>
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

    .content
    {
        /* height: 0vh; */
        transition: .7s;
    }
    .left, .right
    {
        width: 100%;
    }

    .sidebar
    {
        position: relative;
    }

    .list-menu
    {
        display: block;
        width: 100%;
    }
</style>