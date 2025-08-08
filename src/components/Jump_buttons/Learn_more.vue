<template>
  <div class="min-h-screen bg-gray-50 pt-[50px]">
    <!-- About Us -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">About Our Company</h2>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">We're passionate about delivering exceptional value to our
            clients through innovative solutions.</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div v-for="(feature, index) in features" :key="index"
            class="bg-gray-50 p-6 rounded-lg shadow-sm hover:shadow-xl transition all duration-300 ease">
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
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">Comprehensive solutions tailored to your specific needs.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(service, index) in services" :key="index"
            class="bg-white p-6 rounded-lg hover:shadow-xl all duration-300 ease">
            <div
              class="bg-indigo-100 w-12 h-12 rounded-full flex items-center justify-center mb-4 hover:bg-black hover:text-white transition all duration-300 ease">
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
          <div class="hidden md:block absolute top-1/2 left-0 right-0 h-0.5 bg-gray-200 transform -translate-y-1/2">
          </div>
          <div class="grid md:grid-cols-3 gap-8 relative">
            <div v-for="(step, index) in steps" :key="index" class="bg-white">
              <div class="flex flex-col items-center text-center">
                <div
                  class="w-16 h-16 rounded-full bg-indigo-600 hover:bg-indigo-700 text-white flex items-center justify-center text-xl font-bold mb-4 relative transition all duration-300">
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
          <div v-for="(testimonial, index) in testimonials" :key="index"
            class="bg-white p-6 rounded-lg shadow-sm hover:shadow-xl transition all duration-300">
            <div class="flex items-center mb-4">
              <div class="w-12 h-12 rounded-full bg-gray-200 overflow-hidden mr-4">
                <a :href="testimonial.avatar"><img src="../../images/amaresh.jpeg" :alt="testimonial.name"
                    class="w-full h-full object-cover" /></a>
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
        <faq :faqs="faqs"/>
      </div>
    </section>
  </div>
</template>

<script setup>
import multi_cards from '../../multi_cards.json'
import BaseCard from '../common/BaseCard.vue'
import faq from '../common/faq.vue'
import { ref } from 'vue'
const activeFaq = ref(null)
const toggleFaq = (index) => {
  activeFaq.value = activeFaq.value === index ? null : index
}

const features = multi_cards.features
const services = multi_cards.services
const steps = multi_cards.steps
const testimonials = multi_cards.testimonials
const faqs = multi_cards.faqs

</script>
<style>
.hover-shadow:hover {
  box-shadow: 0 0.5rem 1.25rem rgba(0, 0, 0, 0.15) !important;
}

.fw-medium {
  font-weight: 500;
}
</style>
