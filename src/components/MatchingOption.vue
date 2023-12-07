<template>
    <div class="container d-flex" style="justify-content: space-between;">
        <div class="left w-100 pe-3">
            <ul id="items" ref="litems" class="list-group">
                <li class="list-group-item my-1 rounded-0" v-for="(item, index) in props.data.left" :key="index" :data-value="item">{{ item }}</li>
            </ul>
        </div>
        <div class="right w-100 ps-3">
            <ul id="items2" ref="ritems" class="list-group">
                <li class="list-group-item my-1 rounded-0" v-for="(item, index) in props.data.right" :key="index" :data-value="item">{{ item }}</li>
            </ul>
        </div>
    </div>
    <div class="container-fluid d-flex mt-2">
        <!-- <button class="btn btn-primary ms-auto" @click="getResults">ส่งคำตอบ</button> -->
    </div>
</template>
<script setup>
    import { onMounted, ref, defineEmits, defineProps, onBeforeUnmount, watch, computed } from 'vue';
    import Sortable from 'sortablejs';

    const emits = defineEmits(['handleResult']);
    const props = defineProps({
        data: {
            default: {
                left: [],
                right: []
            }
        }
    });

    const data = ref(props.data);
    const selectorData = ref([]);

    const litems = ref();
    const ritems = ref();
    let lSortableInstance;
    let rSortableInstance;

    function getResults() {
        let llist = [];
        let rlist = [];


        // console.log(litems.value);

        
        for (let i = 0; i < litems.value.children.length; i++) {
            llist.push(litems.value.children.item(i).getAttribute('data-value'));
            rlist.push(ritems.value.children.item(i).getAttribute('data-value'));
        }

        let result = llist.map(function (row, index) {
            return [llist[index], rlist[index]];
        });

        // console.log("Result => ");
        // console.log(result);

        // selectorData.value = result.map(function(row){
        //     return {
        //         left: row[0],
        //         right: row[1]
        //     }
        // });

        // selectorData.value.left = result.map(function(row){
        //     return row[0];
        // });

        // selectorData.value.right = result.map(function(row){
        //     return row[1]
        // });

        // console.log("Result => ");
        // console.log(result);

        emits('handleResult', result);
    }

    onMounted(function () {
        getResults(); 

        // Left
        lSortableInstance = new Sortable(litems.value, {
            animation: 150,
            ghostClass: 'bg-info',
            onMove: function (evt) {
                // console.log("Moved => ");
                // console.log(evt);
            },
            onEnd: function (evt) {
                // console.log("End => ");
                // console.log(evt);

                if (evt.oldIndex !== evt.newIndex) {
                    getResults();
                }
            }
        });

        // Right
        rSortableInstance = new Sortable(ritems.value, {
            animation: 150,
            ghostClass: 'bg-info',
            onMove: function (evt) {
                // console.log("Moved => ");
                // console.log(evt);
            },
            onEnd: function (evt) {
                // console.log("End => ");
                // console.log(evt);

                if (evt.oldIndex !== evt.newIndex) {
                    getResults();
                }
            }
        });
    });


    watch(props, function(){
        selectorData.value = props.data;

        // console.log("selectorData => ");
        // console.log(selectorData.value);
    });


    watch(selectorData, function(){
        let llist = [];
        let rlist = [];


        llist = selectorData.value.left.map(function(row){
            return row;
        });

        rlist = selectorData.value.right.map(function(row){
            return row;
        });


        emits('handleResult', llist.map(function(_tmp, index){
            return [llist[index], rlist[index]];
        }));
    });


    // Cleanup Sortable instances when the component is unmounted
    onBeforeUnmount(() => {
        lSortableInstance.destroy();
        rSortableInstance.destroy();
    });
</script>

<style scoped>
    li
    {
        box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
    }
</style>
<style scoped>
    li
    {
        box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
    }
</style>