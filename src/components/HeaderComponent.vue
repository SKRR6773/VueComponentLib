<template>
    <div class="fixed-top">
        <div class="d-flex">
            <SidebarComponent />
            <MenuComponent />
        </div>
    </div>
</template>
<script setup>
    import SidebarComponent from './SidebarComponent.vue';
    import MenuComponent from './menuComponent.vue';
</script>