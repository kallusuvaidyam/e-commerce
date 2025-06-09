<template>
  <div style="
  clip-path: polygon(25% 0%, 100% 0%, 75% 100%, 0% 100%);
  width: 100%;
  height: 400px;
  background-image: url('https://www.svgbackgrounds.com/wp-content/uploads/2021/07/spotlight-mesh-soft-gradient-background.jpg');
  background-size: cover;
  background-position: center;
">
  <div class="w-full max-w-5xl overflow-hidden rounded-lg shadow-lg mx-auto group hover:shadow-2xl transition all duration-300 ease-in-out">
    <h1 class="max-[768px]:text-[16px] text-[20px] font-bold my-3 text-center tracking-widest">Some Trendig Content</h1>
    <div class="slider-track">
      <img
  v-for="(img, index) in duplicatedImages"
  :key="index"
  :src="img"
  alt="slider image"
  class="image w-48 h-72 object-cover mr-2 rounded-md transition-transform duration-200 transform"
/>

    </div>
  </div>
</div>

</template>

<script setup>
import { onMounted } from 'vue';
const images = [
  'https://picsum.photos/200/300?random=1',
  'https://picsum.photos/200/300?random=2',
  'https://picsum.photos/200/300?random=3',
  'https://picsum.photos/200/300?random=4',
  'https://picsum.photos/200/300?random=5',
]

// Duplicate images for smooth loop
const duplicatedImages = [...images, ...images]

// img tilt effect
onMounted(() => {
  const Tilt_images = document.querySelectorAll('.image')
  Tilt_images.forEach((img) => {
    img.addEventListener('mousemove', (e) => {
      const box = img.getBoundingClientRect()
      const X = e.clientX - box.left
      const Y = e.clientY - box.top

      const centerX = box.width / 2
      const centerY = box.height / 2

      const rotateX = -(Y - centerY) / 10
      const rotateY = (X - centerX) / 10

      img.style.transform = `perspective(600px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`
    })

    img.addEventListener("mouseleave", () => {
      img.style.transform = `perspective(600px) rotateX(0deg) rotateY(0deg)`
    })
  })
})

</script>

<style scoped>
@keyframes scroll-left {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-97%);
  }
}

.slider-track {
  @apply flex w-fit;
  animation: scroll-left 20s linear infinite;
}

.group:hover .slider-track {
  animation-play-state: paused;
}

.image {
  transition: transform 0.2s ease;
  will-change: transform;
}

</style>
