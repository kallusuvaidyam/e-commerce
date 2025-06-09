<template>
  <div class="min-h-screen bg-gray-50 pt-[50px]">
    <!-- About Us -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">About Our Company</h2>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">We're passionate about delivering exceptional value to our clients through innovative solutions.</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div v-for="(feature, index) in features" :key="index" class="bg-gray-50 p-6 rounded-lg shadow-sm hover:shadow-xl transition all duration-300 ease">
            <div class="text-indigo-600 mb-4">
              <i :class="[feature.icon, 'text-green-500 text-2xl']"></i>
            </div>
            <h3 class="text-xl font-semibold mb-2">{{ feature.title }}</h3>
            <p class="text-gray-600">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Services -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Our Services</h2>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">Comprehensive solutions tailored to your specific needs.</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(service, index) in services" :key="index" class="bg-white p-6 rounded-lg hover:shadow-xl all duration-300 ease">
            <div class="bg-indigo-100 w-12 h-12 rounded-full flex items-center justify-center mb-4 hover:bg-black hover:text-white transition all duration-300 ease">
              <i :class="service.icon"></i>
            </div>
            <h3 class="text-xl font-semibold mb-2">{{ service.name }}</h3>
            <p class="text-gray-600 mb-4">{{ service.description }}</p>
            <a href="#" class="text-indigo-600 font-medium hover:underline">Learn more →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">How It Works</h2>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">Simple steps to get started with our services.</p>
        </div>

        <div class="relative">
          <div class="hidden md:block absolute top-1/2 left-0 right-0 h-0.5 bg-gray-200 transform -translate-y-1/2"></div>
          <div class="grid md:grid-cols-3 gap-8 relative">
            <div v-for="(step, index) in steps" :key="index" class="bg-white">
              <div class="flex flex-col items-center text-center">
                <div class="w-16 h-16 rounded-full bg-indigo-600 hover:bg-indigo-700 text-white flex items-center justify-center text-xl font-bold mb-4 relative transition all duration-300">
                  {{ index + 1 }}
                </div>
                <h3 class="text-xl font-semibold mb-2">{{ step.title }}</h3>
                <p class="text-gray-600">{{ step.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="py-16 bg-indigo-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">What Our Clients Say</h2>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">Trusted by businesses across various industries.</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(testimonial, index) in testimonials" :key="index" class="bg-white p-6 rounded-lg shadow-sm hover:shadow-xl transition all duration-300">
            <div class="flex items-center mb-4">
              <div class="w-12 h-12 rounded-full bg-gray-200 overflow-hidden mr-4">
                <a :href="testimonial.avatar"><img :src="testimonial.avatar" :alt="testimonial.name" class="w-full h-full object-cover" /></a>
              </div>
              <div>
                <h4 class="font-semibold">{{ testimonial.name }}</h4>
                <p class="text-gray-600 text-sm">{{ testimonial.position }}</p>
              </div>
            </div>
            <p class="text-gray-700 italic">"{{ testimonial.quote }}"</p>
            <div class="flex mt-4 text-yellow-400">
              <span v-for="i in 5" :key="i">★</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="py-16 bg-white">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Frequently Asked Questions</h2>
          <p class="text-lg text-gray-600">Find answers to common questions about our services.</p>
        </div>

        <div class="space-y-4">
          <div v-for="(faq, index) in faqs" :key="index" class="border border-gray-200 rounded-lg overflow-hidden">
            <button @click="toggleFaq(index)" class="w-full px-6 py-4 text-left font-medium text-gray-900 bg-gray-50 hover:bg-gray-100 focus:outline-none flex justify-between items-center">
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
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import clientImg from '@/images/amaresh.jpeg'
import Vrindharak from '@/images/vrindharak.png'
import Ritesh from '@/images/ritesh.png'
const activeFaq = ref(null)

const toggleFaq = (index) => {
  activeFaq.value = activeFaq.value === index ? null : index
}

const features = [
  {
    icon: 'fa fa-line-chart',
    title: 'Data-Driven Approach',
    description: 'We use analytics to make informed decisions that drive results.',
  },
  {
    icon: 'fa fa-cog',
    title: 'Custom Solutions',
    description: 'Tailored services to meet your specific business requirements.',
  },
  {
    icon: 'fas fa-shield-alt',
    title: 'Secure & Reliable',
    description: 'Enterprise-grade security to protect your data and operations.',
  },
]

const services = [
  {
    icon: 'fa fa-cog',
    name: 'Web Development',
    description: 'Custom websites and web applications built with modern technologies.',
  },
  {
    icon: 'fa fa-phone',
    name: 'Mobile Apps',
    description: 'iOS and Android apps that engage your customers.',
  },
  {
    icon: 'fa fa-server',
    name: 'Cloud Solutions',
    description: 'Scalable cloud infrastructure for your growing business.',
  },
]

const steps = [
  {
    title: 'Consultation',
    description: 'We discuss your requirements and goals.',
  },
  {
    title: 'Planning',
    description: 'Our team creates a customized solution plan.',
  },
  {
    title: 'Execution',
    description: 'We implement the solution with regular updates.',
  },
]

const testimonials = [
  {
    name: 'Amaresh Sir',
    position: 'MCA. Qualified.',
    quote: 'Our business grew by 50% after implementing their solutions. Highly recommended!',
    avatar: clientImg,
  },
  {
    name: 'Vrindharak Sir',
    position: 'MCA. Qualified.',
    quote: 'The team delivered exceptional results on time and within budget.',
    avatar: Vrindharak,
  },
  {
    name: 'Ritesh Sir',
    position: 'MCA. Qualified.',
    quote: 'Their expertise helped us scale our operations efficiently.',
    avatar: Ritesh,
  },
]

const faqs = [
  {
    question: 'How much do your services cost?',
    answer: 'Our pricing varies based on project scope and requirements. Contact us for a free quote tailored to your needs.',
  },
  {
    question: 'What industries do you specialize in?',
    answer: 'We have experience across multiple industries including technology, healthcare, finance, and e-commerce.',
  },
  {
    question: 'How long does a typical project take?',
    answer: 'Project timelines depend on complexity, but we always provide estimated delivery dates during our initial consultation.',
  },
]
</script>
<style>
.hover-shadow:hover {
  box-shadow: 0 0.5rem 1.25rem rgba(0, 0, 0, 0.15) !important;
}
.fw-medium {
  font-weight: 500;
}
</style>
