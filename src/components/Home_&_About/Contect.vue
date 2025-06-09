<template>
  <div id="home" class="w-full pt-[65px]">
    <!-- Iframe Section -->
    <div id="map" class="w-full h-[500px] bg-gray-100">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d28729.698034411696!2d84.9202152527402!3d25.82955029857177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3992b33926ee3e39%3A0x526336b7456601d3!2sRahampur%2C%20Bihar%20841202!5e0!3m2!1sen!2sin!4v1748771579795!5m2!1sen!2sin"
        class="w-full h-full"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>

    <!-- Form Section -->
    <div class="max-w-xl mx-auto p-4 sm:p-6 Your email mt-6">
      <h2 class="text-2xl font-semibold mb-4 text-center">Contact Us</h2>

      <form class="max-w-sm mx-auto">
        <div class="mb-5">
          <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
          <input
            v-model="user_data.email"
            type="email"
            id="email"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="email@example.com"
            required
          />
        </div>
        <div class="mb-5">
          <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
          <input
            v-model="user_data.password"
            type="password"
            id="password"
            placeholder="••••••••"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required
          />
        </div>

        <div class="mb-5">
          <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"> Your Message </label>
          <textarea
            v-model="user_data.msg"
            id="message"
            rows="6"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Type your message here..."
          >
          </textarea>
        </div>
        <div class="mb-5">
          <label for="captcha" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            Your Captcha:
            <span class="ml-2 font-mono text-blue-600 bg-gray-100 px-2 py-1 rounded">
              {{ generatedCaptcha }}
            </span>
            <i :style="`transform: rotate(${rotateAngle}deg);`" :class="`fa fa-refresh text-[16px] mt-[10px] ml-[10px] text-green-500 transition all duration-300 ease-in-out`" @click="generateCaptcha"></i>
          </label>
          <input
            v-model="user_data.captcha"
            type="text"
            id="captcha"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Enter CAPTCHA"
            required
          />
        </div>

        <div :class="['text-sm mb-3', isCorrect === true ? 'text-green-600' : isCorrect === false ? 'text-red-600' : '']">
          {{ resultMessage }}
        </div>

        <button
          type="button"
          @click="handle_submit()"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:outline-none font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Submit
        </button>
      </form>
    </div>

    <FaqComponent />

    <!-- Contect Info -->
    <section class="bg-white dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-6xl mx-auto">
        <div class="grid gap-8 sm:grid-cols-2 md:grid-cols-3 text-center">
          <!-- Email -->
          <div class="space-y-2">
            <h2 class="text-xl font-semibold text-gray-800 dark:text-white">Email</h2>
            <p class="text-gray-600 dark:text-gray-300 break-all">
              <a href="mailto:kumarkallu56345@gmail.com" class="hover:underline">kumarkallu56345@gmail.com</a>
            </p>
          </div>

          <!-- Phone -->
          <div class="space-y-2">
            <h2 class="text-xl font-semibold text-gray-800 dark:text-white">Phone</h2>
            <p class="text-gray-600 dark:text-gray-300">
              <a href="tel:+9190665896528" class="hover:underline">+91 90665 896528</a>
            </p>
          </div>

          <!-- Address -->
          <div class="space-y-2">
            <h2 class="text-xl font-semibold text-gray-800 dark:text-white">Office Address</h2>
            <p class="text-gray-600 dark:text-gray-300">Suvaidyam, Garkha, Saran, Bihar, India</p>
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
import FaqComponent from '../ReUsable/FaqComponent.vue'

import useUsers_data from '../Other/composible_api'

const { Contacted_user } = useUsers_data()

const user_data = ref({
  email: '',
  password: '',
  msg: '',
  captcha: '',
})

const generatedCaptcha = ref('')
const resultMessage = ref('')
const isCorrect = ref(null)
const rotateAngle = ref(0)

const generateCaptcha = () => {
  rotateAngle.value += 360
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  generatedCaptcha.value = ''
  for (let i = 0; i < 6; i++) {
    generatedCaptcha.value += chars.charAt(Math.floor(Math.random() * chars.length))
  }
}

const handle_submit = async () => {
  // ?. ka matlab hai:
  // 1. Agar email exist karta hai (undefined/null nahi hai), tab trim() ko call karo.
  // 2. Agar email undefined ya null ho, to trim() call nahi hoga — error nahi aayega, value undefined rahegi.
  const email = user_data.value.email?.trim()
  const password = user_data.value.password?.trim()
  const msg = user_data.value.msg?.trim()
  const captcha = user_data.value.captcha?.trim()

  const isValidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)

  if (!email || !password || !msg || !captcha) {
    resultMessage.value = 'Please fill all data'
    isCorrect.value = false
    return
  }

  if (!isValidEmail) {
    resultMessage.value = 'Please fill a valid email'
    isCorrect.value = false
    return
  }

  if (captcha !== generatedCaptcha.value) {
    resultMessage.value = 'CAPTCHA does not match'
    isCorrect.value = false
    return
  }

  resultMessage.value = 'Form submitted successfully!'
  isCorrect.value = true

  await Contacted_user(user_data.value)

  // Reset form
  user_data.value = {
    email: '',
    password: '',
    msg: '',
    captcha: '',
  }


}


onMounted(() => {
  generateCaptcha()
})
</script>

<style>
.leaflet-container {
  z-index: 0;
}
</style>
