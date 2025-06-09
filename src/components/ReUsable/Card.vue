<template>
  <div class="bg-white dark:bg-gray-800 border dark:border-gray-700 rounded-lg shadow hover:shadow-lg transition-all max-w-full">
    <div class="overflow-hidden w-full h-[220px]">
      <a :href="item.link"><img class="rounded-t-lg w-full hover:scale-[1.1] transition-all" :src="item.image" :alt="item.title" /></a>
    </div>
    <div class="p-5">
      <a :href="item.link"
        ><h5 class="text-2xl font-bold mb-2 text-gray-900 dark:text-white">{{ item.title }}</h5></a
      >
      <p class="mb-3 text-gray-700 dark:text-gray-400">{{ item.description }}</p>
      <a :href="item.link" class="inline-flex items-center px-3 py-2 text-sm font-medium text-white bg-blue-700 rounded-lg hover:bg-blue-800">
        {{ item.buttonText }}
      </a>
    </div>
  </div>
</template>

  <script setup>
defineProps(['item', 'viewMode'])
</script>
