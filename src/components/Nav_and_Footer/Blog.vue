<template>
  <div class="max-w-4xl mx-auto px-4 py-24">
    <!-- Header Section -->
    <header class="mb-8">
      <!-- Title -->
      <h1 class="text-4xl font-bold text-gray-900 mb-4 leading-tight">{{ title }}</h1>

      <!-- Meta Information -->
      <div class="flex flex-wrap items-center text-sm text-gray-600 gap-2 mb-6">
        <div class="flex items-center">
          <i class="fa fa-user text-gray-400 mr-1"></i>
          <span>By <span class="font-medium text-gray-800">{{ author }}</span></span>
        </div>
        <div class="h-1 w-1 bg-gray-400 rounded-full"></div>
        <div class="flex items-center">
          <i class="fa fa-calendar text-gray-400 mr-1"></i>
          <span>{{ formattedDate }}</span>
        </div>
        <div class="h-1 w-1 bg-gray-400 rounded-full"></div>
        <div class="flex items-center">
          <i class="fa fa-clock-o text-gray-400 mr-1"></i>
          <span>{{ readingTime }} min read</span>
        </div>
      </div>

      <!-- Featured Image -->
      <div class="relative rounded-xl overflow-hidden shadow-lg mb-8">
        <img :src="image" :alt="title" class="w-full h-auto aspect-video object-cover" loading="lazy" />
      </div>
    </header>

    <!-- Article Content -->
    <article class="prose prose-lg max-w-none">
      <!-- Introduction -->
      <p class="text-xl text-gray-700 leading-relaxed mb-8">{{ intro }}</p>

      <!-- Main Content Sections -->
      <div v-for="(section, index) in sections" :key="index" class="mb-10">
        <h2 class="text-2xl font-bold text-gray-900 mb-4 pb-2 border-b border-gray-200">{{ section.heading }}</h2>

        <p v-if="section.text" class="text-gray-700 leading-relaxed mb-4">{{ section.text }}</p>

        <ul v-if="section.list" class="space-y-2 mb-4 pl-5">
          <li v-for="(item, i) in section.list" :key="i" class="relative pl-3 text-gray-700">
            <span class="absolute left-0 top-2.5 h-1.5 w-1.5 rounded-full bg-blue-500"></span>
            {{ item }}
          </li>
        </ul>
      </div>

      <!-- FAQ Section -->
      <section class="bg-gray-50 rounded-xl p-6 mb-10">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Frequently Asked Questions</h2>
        <div class="space-y-4">
          <faq :faqs="faqs"/>
        </div>
      </section>
    </article>

    <!-- Tags -->
    <section class="mb-12">
      <h4 class="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4">Article Tags</h4>
      <div class="flex flex-wrap gap-2">
        <a v-for="(tag, i) in tags" :key="i" href="#"
          class="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-medium rounded-full transition">{{ tag }}</a>
      </div>
    </section>

    <!-- Related Articles -->
    <section class="mb-6">
      <h3 class="text-2xl font-bold text-gray-900 mb-6">Recommended Reading</h3>
      <div class="grid md:grid-cols-2 gap-6">
        <article v-for="(post, i) in related" :key="i"
          class="border border-gray-200 rounded-xl overflow-hidden hover:shadow-xl transition all duration-300">
          <a href="https://www.youtube.com/channel/UC_Sqf4rPxuaUs6Itt69CASg" target="_blank" class="block">
            <img :src="post.image" :alt="post.title" class="w-full h-48 object-cover" loading="lazy" />
            <div class="p-6">
              <h4 class="font-bold text-lg mb-2 text-gray-900">{{ post.title }}</h4>
              <p class="text-gray-600 mb-4">{{ post.desc }}</p>
              <span class="text-blue-600 font-medium text-sm inline-flex items-center">
                Read more
                <i class="fa fa-arrow-right ml-1"></i>
              </span>
            </div>
          </a>
        </article>
      </div>
    </section>

    <!-- Author Bio -->
    <section class="border-t border-gray-200 pt-8 mt-8">
      <div class="flex flex-col sm:flex-row gap-6 items-start">
        <img :src="authorImg" alt="Author" class="w-20 h-20 rounded-full object-cover" />
        <div>
          <h4 class="font-bold text-lg text-gray-900 mb-1">About {{ author }}</h4>
          <p class="text-gray-700 mb-3">Full-stack developer with 8+ years of experience building web applications. Specializes in Vue.js and Node.js.</p>
          <div class="flex gap-3">
            <a href="https://github.com/kallu9065586" target="_blank" class="text-gray-500 hover:text-blue-600 transition">
              <i class="fab fa-github"></i>
            </a>
            <a href="https://www.linkedin.com/in/kallu-kumar-106555343/" target="_blank" class="text-gray-500 hover:text-blue-400 transition">
              <i class="fab fa-linkedin"></i>
            </a>
            <a href="https://x.com/kallu69029" target="_blank" class="text-gray-500 hover:text-blue-500 transition">
              <i class="fab fa-twitter"></i>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import authorImg from '@/images/compluter_man_kallu.jpg'

import faq from '../common/faq.vue'
import multi_cardJSON from '../../multi_cards.json'
const title = multi_cardJSON.title
const author = multi_cardJSON.author
const date = multi_cardJSON.date
const image = multi_cardJSON.image
const intro = multi_cardJSON.intro
const sections = multi_cardJSON.sections
const tags = multi_cardJSON.tags
const related = multi_cardJSON.related
const faqs = [
  {
    question: 'How long does it take to learn Vue 3?',
    answer: 'With consistent daily practice of 1-2 hours, most beginners can achieve basic to intermediate proficiency in Vue 3 within 1-2 months.',
  },
  {
    question: 'Which is better for beginners: Vue or React?',
    answer: 'Vue is generally considered more beginner-friendly due to its gentle learning curve, while React has a larger job market. Both are excellent choices for 2025.',
  },
  {
    question: 'Do I need a computer science degree to become a web developer?',
    answer: 'No, many successful web developers are self-taught or complete bootcamps. What matters most is your skill level and portfolio quality.',
  }
]

const activeFAQ = ref(null)

const toggleFAQ = (index) => {
  activeFAQ.value = activeFAQ.value === index ? null : index
}



// Computed properties
const formattedDate = computed(() => {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
})

const readingTime = computed(() => {
  const wordsPerMinute = 200
  const wordCount =
    intro.split(' ').length +
    sections.reduce((acc, section) => {
      return acc + (section.text ? section.text.split(' ').length : 0) + (section.list ? section.list.join(' ').split(' ').length : 0)
    }, 0)
  return Math.ceil(wordCount / wordsPerMinute)
})
</script>

<style>
.prose {
  color: #374151;
}

.prose h2 {
  color: #111827;
  margin-top: 2em;
  margin-bottom: 1em;
}

.prose p {
  margin-bottom: 1.25em;
  line-height: 1.7;
}
</style>
