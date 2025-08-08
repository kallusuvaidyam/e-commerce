<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-6">
    <h2 class="text-4xl font-bold text-gray-800 mb-1 text-[22px] tracking-widest text-center">Our Services</h2>
    <div v-for="(item, index) in items" :key="index"
      class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition duration-300 w-[70%] max-[768px]:w-full mx-auto">
      <template v-if="type === 'service'">
        <div class="text-4xl mb-4 text-center">{{ item.icon }}</div>
        <h3 class="text-xl font-semibold text-gray-800 mb-2 text-center">{{ item.title }}</h3>
        <p class="text-gray-600 text-center">{{ item.description }}</p>
      </template>

      <template v-else-if="type === 'testimonial'">
        <p class="text-gray-600 italic mb-4">"{{ item.message }}"</p>
        <a :href="item.link" target="_blank">
          <div class="flex items-center">
            <img :src="item.image" alt="Client" class="w-12 h-12 rounded-full mr-4" />
            <div>
              <p class="font-semibold">{{ item.name }}</p>
              <p class="text-sm text-gray-500">{{ item.role }}</p>
            </div>
          </div>
        </a>
      </template>

      <template v-else-if="type === 'pricing'">
        <h3 class="text-xl font-semibold text-center mb-4">{{ item.name }}</h3>
        <p :class="'text-center text-3xl font-bold ' + item.color">{{ item.price }}</p>
        <ul class="mt-6 space-y-4 text-gray-600">
          <li v-for="(f, i) in item.features" :key="i">{{ f }}</li>
        </ul>
        <button
          :class="'w-full mt-6 ' + item.buttonColor + ' text-white py-3 rounded-lg hover:' + item.hoverColor + ' transition duration-300'">Get
          Started</button>
      </template>
    </div>
  </div>
</template>

<script setup>
defineProps({ items: Array, type: String })
</script>
