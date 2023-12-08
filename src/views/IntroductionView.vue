<template>
    <div>
        <div class="mt-3 h-100">
            <header>
                <h1><strong>Introduction</strong></h1>
            </header>
            <div class="container mt-3" style="overflow: auto;" id="intro.exam">
                <header class="mb-3">
                    <h2 class="text-secondary">#Example: </h2>
                </header>
                <div class="row">
                    <div class="col-sm-12 col-md-6">
                        <div class="left me-5">
                            <textarea id="" cols="30" rows="10" style="width: 100%;" @input="" v-model="textareaData">
                                
                            </textarea>
                            <SelectOptionWritterVue :raw_text.sync="textareaData" />
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-6">
                        <div class="right ms-5">
                            <!-- <TestCompo /> -->
                            <MatchingOption @handleResult="handleResult" :data="testData" />
                
                            {{ matchingValue }}
                        </div>
                    </div>
                </div>
            </div><hr>
            <div class="mt-3">
                <h3 align="center" class="d-block w-100"><strong style="font-size: 50px;">TEST</strong></h3>
                <div class="mt-3">
            
                    <TestView />
                </div>
            </div>
        </div>
    
    
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" ref="toastEl" class="toast" role="alert">
                <div class="toast-header">
                    <strong>Save to Save?</strong>
                </div>
                <div class="toast-body">
                    Save Example Word To Successfully!
    
                    <!-- {{ matchingValue }} -->
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
    import { ref, watch, onMounted } from 'vue';
    import axios from 'axios';
    import { Toast } from 'bootstrap';

    import SelectOptionWritterVue from './../components/SelectOptionWritter.vue';
    import TestView from './../views/TestView.vue';

    const toastEl = ref();
    const matchingValue = ref([]);


    const testData = ref({
        left: [
            "9 + 9",
            "20 + 4",
            "6 + 3",
            "18 + 2",
            "9 + 7"
        ],
        right: [
            "24",
            "9",
            "18",
            "16",
            "20"
        ]
    });


    function handleResult(result)
    {
        // console.log("result => ");
        // console.log(result);

        matchingValue.value = result;
    }


    let update_exam_word_interval;
    const textareaData = ref('');

    watch(textareaData, function(){
        if (update_exam_word_interval !== null)
        {
            clearTimeout(update_exam_word_interval);

        }


        update_exam_word_interval = setTimeout(function(){

            let formData = new FormData;
            formData.append("word_data", textareaData.value);
    
    
            axios({
                url: "http://localhost:7755/update_exam_word",
                method: "POST",
                data: formData
            }).then(function(response){
                (new Toast(toastEl.value, {
                    delay: 1000
                })).show();
            }).catch(function(err){
                console.error(err);
            });
        }, 1000);
    });


    onMounted(function(){
        axios({
            url: 'http://localhost:7755/exam_word',
            method: "POST"
        }).then(function(response){
            textareaData.value = response.data;
        }).catch(function(err){
            console.error(err);
        });
    });
</script>