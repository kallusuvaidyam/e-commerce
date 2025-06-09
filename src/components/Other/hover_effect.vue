<template>
  <!-- <div class="w-4 h-4 bg-green-400 fixed z-100 rounded-full">

  </div> -->
  <span ref="cursor" class="w-10 h-10 bg-gray-600 z-100 absolute rounded-full pointer-events-none"></span>
</template>

<script setup>
import { onMounted, ref } from 'vue'
const cursor = ref(null)

onMounted(() => {
  document.addEventListener('mousemove', (e) => {
    if (cursor.value) {
      cursor.value.style.left = `${e.pageX - 20}px`
      cursor.value.style.top = `${e.pageY -20}px`
      console.log(cursor.value)
    }
  })
})
</script>

<style>
span {
  filter: blur(30px);
  position: absolute;
  transition: transform 0.05s ease-out;
}
</style>
