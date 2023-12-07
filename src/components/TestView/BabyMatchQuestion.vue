<template>
    <form @submit.prevent="submit">
        <div>
            <header>
                <h5>1.) จับคู่ข้อที่ถูกต้องที่สุด?</h5>
            </header>
            <div class="question">
                <MatchingOption :data.sync="data" @handleResult="handleResult" />
            </div>
            <div class="mx-2 d-flex">
                <button class="btn btn-success rounded-0 ms-auto">ส่งคำตอบ</button>
            </div>
        </div>
    </form>
</template>
<script setup>
    import { onMounted, ref } from 'vue';
    import axios from 'axios';
    import MatchingOption from '../MatchingOption.vue';
    import Swal from 'sweetalert2';


    const data = ref();
    const resultValue = ref();

    function handleResult(result)
    {
        console.log("handle Result => ");
        console.log(result);
        resultValue.value = result;
    }

    function submit(e)
    {
        console.log(e);
        console.log(resultValue.value);

        let formData = new FormData;
        formData.append("answer", JSON.stringify(resultValue.value));

        axios({
            url: "http://localhost:7700/chk_options",
            method: "POST",
            data: formData
        }).then(function(response){
            if (response.data)
            {
                Swal.fire({
                    icon: "success",
                    title: "Very Much!, You correct!"
                });
            }
            else
            {
                Swal.fire({
                    icon: "error",
                    title: "Not Correct"
                });
            }
        }).catch(function(err){
            console.error(err);
        });
    }

    onMounted(function(){
        axios.get("http://localhost:7700/exam_options", ).then(function(response){
            // console.log(response.data);
            data.value = response.data;
        }).catch(function(err){
            console.error(err);
        });
    });
</script>