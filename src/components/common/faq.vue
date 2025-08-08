<template>
  <div class="space-y-4">
    <div v-for="(faq, index) in faqs" :key="index" class="border border-gray-200 rounded-lg overflow-hidden">
      <button @click="toggleFaq(index)"
        class="w-full px-6 py-4 text-left font-medium text-gray-900 bg-gray-50 hover:bg-gray-100 focus:outline-none flex justify-between items-center">
        <span>{{ faq.question }}</span>
        <span class="transform transition-transform duration-200" :class="{ 'rotate-180': activeFaq === index }">
          <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </span>
      </button>
      <div v-show="activeFaq === index" class="px-6 py-4 bg-white">
        <p class="text-gray-600">{{ faq.answer }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  faqs: {
    type: Array,
    required: true,
  },
})

const activeFaq = ref(null)

function toggleFaq(index) {
  activeFaq.value = activeFaq.value === index ? null : index
}
</script>
