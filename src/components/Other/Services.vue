<template>
  <div>
    <!-- Services Summary -->
    <CardGrid :items="services" type="service" />

    <!-- Choose Us Section -->
    <section class="max-w-4xl mx-auto my-10 px-4 hover:shadow-xl transition all duration-300 ease py-6">
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
        <button class="mx-3 bg-blue-500 text-white py-3 px-8 rounded-lg text-lg font-semibold hover:bg-blue-600 transition duration-300">Get a Quote</button>
      </a>
      <router-link :to="{ path: '/contact' }">
        <button class="mx-3 bg-gray-800 text-white py-3 px-8 rounded-lg text-lg font-semibold hover:bg-gray-700 mt-4 sm:mt-0 sm:ml-4 transition duration-300">Contact Us</button>
      </router-link>
      <a href="https://kalluweb.vercel.app/" target="_blank">
        <button class="mx-3 bg-green-500 text-white py-3 px-8 rounded-lg text-lg font-semibold hover:bg-green-600 mt-4 sm:mt-0 sm:ml-4 transition duration-300">Start Project</button>
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

const services = [
  { icon: '🛠️', title: 'Web Development', description: 'Custom websites...' },
  { icon: '📱', title: 'Mobile App Development', description: 'Cross-platform apps...' },
  { icon: '🎨', title: 'UI/UX Design', description: 'User-friendly designs...' },
  { icon: '🛒', title: 'E-commerce Solutions', description: 'Online stores...' },
  { icon: '🔧', title: 'Website Maintenance', description: 'Ongoing support...' },
]

const reasons = [
  { icon: '⚡', title: 'Fast Delivery', description: 'Projects on time.' },
  { icon: '💰', title: 'Affordable Pricing', description: 'Budget-friendly rates.' },
  { icon: '🧠', title: 'Modern Tech Stack', description: 'Using Vue.js, Flask...' },
  { icon: '🛠️', title: 'Ongoing Support', description: 'We support your product.' },
]

const testimonials = [
  { message: 'This team helped...', name: 'Kallu', role: 'Developer', image: 'src/images/compluter_man_kallu.jpg', link: 'https://www.instagram.com/mrkkgupta2023/' },
  { message: 'The app they built...', name: "Kallu's marks", role: 'Kallu', image: 'src/images/marks.jpg', link: 'https://www.instagram.com/mrkkgupta2023/' },
  { message: 'They delivered...', name: 'Suvaidyam', role: 'Company (Delhi)', image: 'src/images/suvaidyam.jpeg', link: 'https://www.suvaidyam.com/' },
]

const pricingPlans = [
  { name: 'Basic Plan', price: '$99/month', features: ['1 Custom Website', 'Responsive Design', 'Basic Support', '1 Revision'], buttonColor: 'bg-blue-500', hoverColor: 'bg-blue-600' },
  { name: 'Standard Plan', price: '$199/month', features: ['3 Websites', 'Responsive Design', 'Advanced Support', '2 Revisions'], buttonColor: 'bg-green-500', hoverColor: 'bg-green-600' },
  { name: 'Premium Plan', price: '$399/month', features: ['Unlimited Websites', 'Responsive Design', '24/7 Support', 'Unlimited Revisions'], buttonColor: 'bg-purple-500', hoverColor: 'bg-purple-600' },
]
</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: Sofia;
}
</style>
