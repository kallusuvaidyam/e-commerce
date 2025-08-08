<template>
  <div :class="div_class">
    <div class="overflow-hidden w-full h-[220px]">
      <a href="#" class=""><img :class="`${img_class}`" :src="image" alt="Ply bord" /></a>
    </div>
    <div class="p-5">
      <a href="#">
        <h5 :class="h5_class">{{ title }}</h5>
      </a>
      <p :class="[p_class]">{{ subtitle }}</p>
      <p :class="p_class">{{ description }}</p>
      <a href="#" :class="a_class">{{ buttonText }}</a>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(["title", "div_class", "img_class", "image", "h5_class", "p_class", "subtitle", "description", "a_class", "buttonText"])
import { ref } from 'vue';

</script>