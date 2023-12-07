<template>
    <form @submit.prevent="submit">
        <div>
            <header>
                <h5>2.) ใส่คำตอบที่ถูกต้องลงในช่องว่าง</h5>
            </header>
            <div class="question">
                <SelectOptionWritter :raw_text="raw_text" />
            </div>
            <div class="mx-2 d-flex">
                <button class="btn btn-success rounded-0 ms-auto">ส่งคำตอบ</button>
            </div>
        </div>
    </form>
</template>
<script setup>
    import SelectOptionWritter from '../SelectOptionWritter.vue';
    import axios from 'axios';
    import Swal from 'sweetalert2';
    import { onMounted, ref } from 'vue';


    const raw_text = ref("");



    function submit(e)
    {
        let formData = new FormData(e.target);

        console.log(import.meta.env.VITE_APP_API_URL);

        axios({
            url: import.meta.env.VITE_APP_API_URL + "/chk_exam_word",
            method: 'POST',
            data: formData
        }).then(function(response){
            Swal.fire({
                icon: response.data ? "success" : "error",
                title: response.data ? "You Correct" : "You Not Correct!",
            });
        }).catch(function(err){
            console.error(err);
        });
    }

    onMounted(function(){
        axios({
            url: "http://localhost:7700/exam_word",
            method: "POST",
        }).then(function(response){
            raw_text.value = response.data;
        }).catch(function(err){
            console.error(err);
        });
    });

</script>