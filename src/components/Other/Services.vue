<template>
  <div>
    <!-- Services Summary -->
    <CardGrid :items="services" type="service" />

    <!-- Choose Us Section -->
    <section class="w-[70%] mx-auto my-10 px-4 hover:shadow-xl transition all duration-300 ease py-6">
      <h2 class="text-2xl font-bold text-center mb-6">Why Choose Us?</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div v-for="(reason, index) in reasons" :key="index" class="flex items-start gap-4">
          <span :class="' text-2xl'">{{ reason.icon }}</span>
          <div>
            <h3 class="font-semibold">{{ reason.title }}</h3>
            <p class="text-gray-600 text-sm">{{ reason.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Action Buttons -->
    <div class="text-center mt-8">
      <a href="https://www.youtube.com/channel/UC_Sqf4rPxuaUs6Itt69CASg" tar>
        <button
          class="mx-3 bg-blue-500 text-white py-3 px-8 rounded-lg text-lg font-semibold hover:bg-blue-600 transition duration-300">
          Get a Quote
        </button>
      </a>
      <router-link :to="{ path: '/contact' }">
        <button
          class="mx-3 bg-gray-800 text-white py-3 px-8 rounded-lg text-lg font-semibold hover:bg-gray-700 mt-4 sm:mt-0 sm:ml-4 transition duration-300">
          Contact Us
        </button>
      </router-link>
      <a href="https://kalluweb.vercel.app/" target="_blank">
        <button
          class="mx-3 bg-green-500 text-white py-3 px-8 rounded-lg text-lg font-semibold hover:bg-green-600 mt-4 sm:mt-0 sm:ml-4 transition duration-300">
          Start Project
        </button>
      </a>
    </div>

    <!-- Testimonials -->
    <CardGrid :items="testimonials" type="testimonial" />

    <!-- Pricing -->
    <CardGrid :items="pricingPlans" type="pricing" />
  </div>
</template>

<script setup>
import CardGrid from '../ReUsable/CardGrid.vue'
import servicesJSON from './services.json'

const services = servicesJSON.services
const reasons = servicesJSON.reasons
const testimonials = servicesJSON.testimonials
const pricingPlans = servicesJSON.pricingPlans

</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: Sofia;
}
</style>
