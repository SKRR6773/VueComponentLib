<template>
    <div v-html="htmlContent"></div>
</template>
<script setup>
    import { defineProps, computed } from 'vue';
    import modules from '../lib/modules';

    const props = defineProps({
        raw_text: {
            type: String,
            defaultValue: "Hello World!"
        }
    });
    // const htmlContent = ref('');
    const regex_json = /{(?:[^{}"]|"(?:\\.|[^"\\])*")*: ?(?:[^{}"]|"(?:\\.|[^"\\])*")*}/g;


    const htmlContent = computed(function(){
        // props.raw_text;

        // console.log(props.raw_text.match(regex_json));

        return props.raw_text.replace(regex_json, function(same){
            if (modules.try_json_parse(same))
            {
                let obj = JSON.parse(same);
                let keynames = Object.keys(obj);
                let values = Object.values(obj);

                let keyname = keynames[0];
                let value = values[0];


                if (value.constructor === Array)
                {
                    let selectEl = document.createElement('select');
                    selectEl.setAttribute('data-mrg-select', keyname);
                    selectEl.name = keyname;

                    for (let i=0; i < value.length; i++)
                    {
                        if (value[i].constructor === String)
                        {
                            let optionEl = document.createElement('option');
                            optionEl.textContent = value[i];
                            optionEl.value = value[i];



                            selectEl.appendChild(optionEl);
                        }
                    }


                    return selectEl.outerHTML;
                }
                else
                {
                    return "##N##";
                }
            }
            return "## เกือบแล้วอีกนิดเดียว ##";
        });
    });


    document.addEventListener('change', function(e){
        if (e.target.getAttribute('data-mrg-select') !== null)
        {
            document.querySelectorAll('[data-mrg-select=a]').forEach(function(elem){
                elem.value = e.target.value;
            });
        }
    });

</script>