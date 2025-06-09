<template>
  <div class="max-w-2xl mx-auto bg-white shadow-xl rounded-xl p-6">
    <h2 class="text-2xl font-bold mb-4 text-center tracking-wider">❓ Frequently Asked Questions</h2>

    <div class="space-y-4">
      <div
        v-for="(faq, index) in faqs"
        :key="index"
        class="faq-item border rounded-lg p-4 cursor-pointer bg-gray-50 hover:shadow-xl transition-all duration-300"
        :class="{ 'bg-gray-50': openIndex === index }"
        @click="toggleFaq(index)"
      >
        <div class="faq-question font-semibold text-lg text-gray-700">
          {{ faq.question }}
        </div>

        <div
          class="faq-answer mt-2 text-gray-700 overflow-hidden transition-all duration-300"
          :style="openIndex === index ? 'max-height: 200px;' : 'max-height: 0;'"
        >
          <p v-if="openIndex === index" class="text-gray-500">{{ faq.answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const faqs = ref([
  {
    question: 'Q1: Website banane me kitna time lagta hai?',
    answer: 'Ye aapke requirements par depend karta hai. Simple website 3-5 din me ban sakti hai.',
  },
  {
    question: 'Q2: Kya aap mobile-friendly design banate ho?',
    answer: 'Haan, hamari saari websites mobile responsive hoti hain.',
  },
  {
    question: 'Q3: Kya SEO optimize website milegi?',
    answer: 'Bilkul, hum SEO best practices follow karte hain har project me.',
  },
])

const openIndex = ref(0)

const toggleFaq = (index) => {
  openIndex.value = openIndex.value === index ? -1 : index
}
</script>
