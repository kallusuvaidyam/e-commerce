<template>
  <div id="home" class="w-full pt-[65px]">
    <!-- Iframe Section -->
    <div id="map" class="w-full h-[500px] bg-gray-100">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d28729.698034411696!2d84.9202152527402!3d25.82955029857177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3992b33926ee3e39%3A0x526336b7456601d3!2sRahampur%2C%20Bihar%20841202!5e0!3m2!1sen!2sin!4v1748771579795!5m2!1sen!2sin"
        class="w-full h-full" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>

    <!-- Form Section -->
    <div class="max-w-xl mx-auto p-4 sm:p-6 Your email mt-6">
      <h2 class="text-2xl font-semibold mb-4 text-center">Contact Us</h2>
      <FormInput v-model="user_data" :fields="fields" submitText="Submit" @submit="submitData" />
    </div>


    <!-- Contect Info -->
    <section class="bg-white dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-6xl mx-auto">
        <div class="grid gap-8 sm:grid-cols-2 md:grid-cols-3 text-center">
          <!-- Email -->
          <div class="space-y-2">
            <h2 class="ContactH2Class">Email</h2>
            <p class="ContactPClass break-all">
              <a href="mailto:kumarkallu56345@gmail.com" class="hover:underline">kumarkallu56345@gmail.com</a>
            </p>
          </div>

          <!-- Phone -->
          <div class="space-y-2">
            <h2 class="ContactH2Class">Phone</h2>
            <p class="ContactPClass">
              <a href="tel:+9190665896528" class="hover:underline">+91 90665 896528</a>
            </p>
          </div>

          <!-- Address -->
          <div class="space-y-2">
            <h2 class="ContactH2Class">Office Address</h2>
            <p class="ContactPClass">Suvaidyam, Garkha, Saran, Bihar, India</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// import Captcha from '../Other/Captcha.vue'
import { onMounted } from 'vue'
import { ref } from 'vue'
import FormInput from '../common/FormInput.vue'
const ContactH2Class = 'text-xl font-semibold text-gray-800 dark:text-white'
const ContactPClass = 'text-gray-600 dark:text-gray-300'

const fields = [
  { name: 'email', label: 'Email', type: 'email', placeholder: 'Your email' },
  { name: 'password', label: 'Password', type: 'password', placeholder: 'Your password' },
  { name: 'message', label: 'Message', type: 'text', placeholder: 'Your message' },
]

const user_data = ref({})

const submitData = async (data) => {
  console.log(data, "/////////////////////////////////////");
  
  data.email = ''
  data.message = ''
  data.password = ''
}

console.log(history.state.back);
</script>

<style>
</style>
