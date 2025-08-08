<template>
  <div class="p-6">
    <i :class="[isGrid ? 'fa fa-list' : 'fa fa-th', 'text-2xl']" @click="isGrid = !isGrid"></i>
    <div :class="[isGrid ? 'grid xl:grid-cols-4 2x:grid-cols-5 md:grid-cols-2 lg:grid-cols-3 gap-4' : 'flex flex-col']">
      <div v-for="post in posts" :key="post.id" class="p-4 border rounded shadow">
        <h2 class="text-lg font-semibold">{{ post.title }}</h2>
        <p class="text-gray-600">{{ post.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isGrid = ref(true)
const posts = [
  { id: 1, title: 'Vue 3 Basics', description: 'Learn Vue 3 step-by-step' },
  { id: 2, title: 'Tailwind CSS Tips', description: 'Design fast with Tailwind' },
  { id: 3, title: 'Composition API', description: 'Use Vue 3 Composition API effectively' },
  { id: 4, title: 'Pinia Basics', description: 'State management with Pinia' },
  { id: 5, title: 'Routing in Vue', description: 'Using Vue Router in apps' },
  { id: 6, title: 'Vue Lifecycle', description: 'Understanding component lifecycle' },
]
</script>
