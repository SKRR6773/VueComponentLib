<template>
    <div class="container-fluid">
        <div class="row gy-3">
            <div class="col-sm-12 col-md-12">
                <div class="left w-100">
                    <BabyMatchQuestion />
                </div>
            </div><hr>
            <div class="col-sm-12 col-md-12">
                <div class="right w-100 mt-5 sm-mt-0">
                    <SelectQuestion />
                </div>
            </div>
        </div>
    </div>
    <div>
        <div class="shadow">
            <img :src="CodeSrcImage" class="w-100 rounded-3 img-thumbnail" style="pointer-events: none;">
        </div>
    </div>
</template>
<script setup>
    import { onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import BabyMatchQuestion from '../components/TestView/BabyMatchQuestion.vue';
    import SelectQuestion from '../components/TestView/SelectQuestion.vue';
    import CodeSrcImage from '../assets/code.png';


    const route = useRoute();

    
    onMounted(function(){
        console.log(route.params);
        // alert(route.params.id);
    });

</script>