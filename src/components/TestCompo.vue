<template>
    <div class="container">
        <div style="width: 100%;">
            <div class="d-flex mb-5" style="justify-content: space-between;"> <!-- row -->
                <div>
                    <span class="me-2">A</span>
                    <input type="radio" name="" id="" @click="radioClick">
                </div>
                <div>
                    <input type="radio" name="" id="">
                    <span class="ms-2">Z</span>
                </div>
            </div>
            <div class="d-flex mb-5" style="justify-content: space-between;"> <!-- row -->
                <div>
                    <span class="me-2">B</span>
                    <input type="radio" name="" id="">
                </div>
                <div>
                    <input type="radio" name="" id="">
                    <span class="ms-2">Y</span>
                </div>
            </div>
            <div class="d-flex mb-5" style="justify-content: space-between;"> <!-- row -->
                <div>
                    <span class="me-2">C</span>
                    <input type="radio" name="" id="">
                </div>
                <div>
                    <input type="radio" name="" id="">
                    <span class="ms-2">X</span>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
    function radioClick(e)
    {
        console.log(e);
    }
</script>
<style scoped>
    
</style>