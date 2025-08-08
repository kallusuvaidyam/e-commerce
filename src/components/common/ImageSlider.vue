<template>
  <section id="slider" class="w-full h-[500px] bg-red-300 pt-[65px] flex items-center justify-center">
    <div class="relative w-full h-full overflow-hidden slider-container">

      <!-- Images -->
      <img v-for="(img, i) in images" :key="i" :src="img" :class="[
        'absolute inset-0 w-full h-full object-cover transition-opacity duration-700 ease-in-out',
        i === currentIndex ? 'opacity-100 z-10' : 'opacity-0 z-0'
      ]" />

      <!-- Left Navigation Button -->
      <button @click="prevImage"
        class="absolute top-1/2 left-4 -translate-y-1/2 bg-white/70 hover:bg-white rounded-full p-3 shadow z-10">
        <i class="fa fa-chevron-left text-2xl text-gray-700"></i>
      </button>

      <!-- Right Navigation Button -->
      <button @click="nextImage"
        class="absolute top-1/2 right-4 -translate-y-1/2 bg-white/70 hover:bg-white rounded-full p-3 shadow z-10">
        <i class="fa fa-chevron-right text-2xl text-gray-700"></i>
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'

const props = defineProps({
  images: {
    type: Array,
    required: true
  }
})

const currentIndex = ref(0)
let intervalId = ref(null)

const nextImage = () => {
  currentIndex.value = (currentIndex.value + 1) % props.images.length
  resetInterval()
}

const prevImage = () => {
  currentIndex.value = (currentIndex.value - 1 + props.images.length) % props.images.length
  resetInterval()
}

const resetInterval = () => {
  if (intervalId.value) clearInterval(intervalId.value)
  intervalId.value = setInterval(nextImage, 3000)
}

onMounted(() => {
  if (props.images.length > 0) {
    resetInterval()
  }
})

onBeforeUnmount(() => {
  if (intervalId.value) clearInterval(intervalId.value)
})
</script>
