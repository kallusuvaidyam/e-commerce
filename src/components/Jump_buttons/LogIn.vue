<template>
  <div class="login_form w-full bg-gray-50 p-6 pt-[100px]">
    <form class="max-w-sm mx-auto space-y-4 border border-gray-400 rounded p-6 hover:shadow-xl transition all duration-300 ease">
      <!-- Name Field -->
      <div>
        <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Name*</label>
        <div class="relative">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 10a4 4 0 100-8 4 4 0 000 8zm0 2c-4 0-7 2-7 4v1h14v-1c0-2-3-4-7-4z" />
            </svg>
          </div>
          <input
            type="text"
            id="name"
            v-model="formData.name"
            placeholder="Your Name"
            required
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            :class="{ 'border-red-500': errors.name }"
          />
        </div>
        <p v-if="errors.name" class="text-red-500 text-xs mt-1">{{ errors.name }}</p>
      </div>

      <!-- Email Field -->
      <div>
        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Email*</label>
        <div class="relative">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 16">
              <path d="M0 4v8a2 2 0 002 2h16a2 2 0 002-2V4l-10 6L0 4zM0 2l10 6 10-6V0H0v2z" />
            </svg>
          </div>
          <input
            v-model="formData.email"
            type="email"
            id="email"
            required
            placeholder="email@example.com"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            :class="{ 'border-red-500': errors.email }"
          />
        </div>
        <p v-if="errors.email" class="text-red-500 text-xs mt-1">{{ errors.email }}</p>
      </div>

      <!-- Password Field -->
      <div>
        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Password*</label>
        <div class="mb-1 w-full h-[2px] bg-gray-300 mt-1 rounded" :class="{ hidden: !passwordFocused }">
          <div :class="[passwordStrengthColor]" :style="{ width: passwordStrengthPercent }" class="h-full transition-all duration-300 rounded"></div>
        </div>
        <div class="relative">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 1a5 5 0 00-5 5v4H5a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2V12a2 2 0 00-2-2h-2V6a5 5 0 00-5-5zm-3 5a3 3 0 116 0v4H9V6zm6 10a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <div class="absolute inset-y-0 end-0 flex items-center space-x-2 pe-2">
            <button @click="showPassword = !showPassword" type="button" class="text-gray-600 hover:text-gray-900 text-sm">
              {{ showPassword ? '🙈' : '👁' }}
            </button>
            <button @click="RotateAndGenerate" type="button" :class="['rounded transform transition duration-500 text-gray-600 hover:text-gray-900 text-sm', isRotated ? 'rotate-[360deg]' : 'rotate-0']">🔄</button>
          </div>
          <input
            v-model="formData.password"
            :type="showPassword ? 'text' : 'password'"
            id="password"
            required
            placeholder="••••••••"
            @focus="passwordFocused = true"
            @blur="passwordFocused = false"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 pe-20 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            :class="{ 'border-red-500': errors.password }"
          />
        </div>
      </div>
      <p v-if="errors.password" class="text-red-500 text-xs mt-1">{{ errors.password }}</p>
      <!-- Phone Field -->
      <div>
        <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Phone Number*</label>
        <div class="relative">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M6.62 10.79a15.533 15.533 0 006.59 6.59l2.2-2.2a1 1 0 011.11-.21 11.36 11.36 0 003.55.57 1 1 0 011 1v3.61a1 1 0 01-.89 1 19.86 19.86 0 01-8.59-2.71 19.53 19.53 0 01-6-6 19.86 19.86 0 01-2.71-8.59A1 1 0 013.43 2h3.61a1 1 0 011 1 11.36 11.36 0 00.57 3.55 1 1 0 01-.21 1.11l-2.2 2.2z"
              />
            </svg>
          </div>
          <input
            v-model="formData.phone"
            type="tel"
            id="phone"
            placeholder="+91 9876543210"
            @input="formatPhoneNumber"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            :class="{ 'border-red-500': errors.phone }"
          />
        </div>
        <p v-if="errors.phone" class="text-red-500 text-xs mt-1">{{ errors.phone }}</p>
      </div>

      <!-- Address Field -->
      <div>
        <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Address(Optional)</label>
        <div class="relative">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 3l9 9-1.5 1.5L18 12.5V20h-5v-5H11v5H6v-7.5l-1.5 1.5L3 12l9-9z" />
            </svg>
          </div>
          <input
            v-model="formData.address"
            type="text"
            id="address"
            placeholder="123 Main St, City"
            class="outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
          />
        </div>
      </div>

      <!-- Status Message -->
      <p v-if="message" class="text-sm" :class="error ? 'text-red-500' : 'text-green-500'">{{ message }}</p>

      <!-- Action Buttons -->
      <div class="flex space-x-2">
        <button type="button" @click="resetForm" class="focus:outline-none text-white bg-gray-500 hover:bg-gray-600 font-medium rounded-lg text-sm px-5 py-2.5 me-2 dark:bg-gray-600 dark:hover:bg-gray-700">Reset</button>
        <button type="button" @click="submitForm" class="focus:outline-none text-white bg-green-700 hover:bg-green-800 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700">
          Submit
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import useUsers_data from '../Other/composible_api'

const { add_user } = useUsers_data()
const isRotated = ref(false)

// Form Data
const formData = ref({
  name: '',
  email: '',
  password: '',
  phone: '',
  address: '',
})

// UI States
const showPassword = ref(false)
const passwordFocused = ref(false)
const message = ref('')
const error = ref(false)

const errors = ref({
  name: '',
  email: '',
  phone: '',
  password: '',
})

const passwordChecks = computed(() => {
  const pass = formData.value.password.trim()
  return [/[0-9]/.test(pass), /[A-Z]/.test(pass), /[a-z]/.test(pass)]
})

const passwordStrengthColor = computed(() => {
  const score = passwordChecks.value.filter(Boolean).length
  return ['bg-gray-300', 'bg-red-500', 'bg-orange-500', 'bg-green-500'][score]
})

const passwordStrengthPercent = computed(() => {
  const score = passwordChecks.value.filter(Boolean).length
  return ['0%', '33%', '66%', '100%'][score]
})

// Password Methods
const generatePassword = () => {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-='
  formData.value.password = Array.from({ length: 12 }, () => chars[Math.floor(Math.random() * chars.length)]).join('')
}

const RotateAndGenerate = () => {
  generatePassword()
  isRotated.value = !isRotated.value
}

// Phone Formatting
const formatPhoneNumber = () => {
  const digitsOnly = formData.value.phone.replace(/\D/g, '')
  formData.value.phone = digitsOnly.replace(/(\d{2})(\d{5})(\d{4})/, '+91 $1 $2-$3')
}

// Form Validation
const validateForm = () => {
  let valid = true
  errors.value = { name: '', email: '', phone: '', password: '' }

  // Name validation
  if (!formData.value.name.trim()) {
    errors.value.name = 'Name is required'
    valid = false
  } else if (!/^[A-Za-z ]+$/.test(formData.value.name)) {
    errors.value.name = 'Name should only contain letters and spaces'
    valid = false
  }

  // Email validation
  if (!formData.value.email) {
    errors.value.email = 'Email is required'
    valid = false
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.email)) {
    errors.value.email = 'Invalid email address'
    valid = false
  }

  // Phone validation
  const cleanedPhone = formData.value.phone.replace(/\s|-/g, '') // remove space and dashes

  if (!cleanedPhone) {
    errors.value.phone = 'Phone is required'
    valid = false
  } else if (!/^(?:\+91|91)?[6-9]\d{9}$/.test(cleanedPhone.replace(/\D/g, ''))) {
    errors.value.phone = 'Invalid phone number (should be 10 digits starting with 6-9, optional +91)'
    valid = false
  }

  if (!formData.value.password) {
    errors.value.password = 'Password is required'
    valid = false
  }

  return valid
}

import { useRouter } from 'vue-router'
const router = useRouter()

// CRUD Operations
const submitForm = async () => {
  if (!validateForm()) {
    error.value = true
    message.value = 'Please fix the errors'
    return
  }

  try {
    await add_user(formData.value)

    // Show success message
    error.value = false
    message.value = 'Login successful! Redirecting...'

    localStorage.setItem('user_info', JSON.stringify(formData.value))

    let user = localStorage.getItem('user_info')

    if (user) {
      router.push('/')
      // window.location.reload()
    }
  } catch (err) {
    error.value = true
    message.value = 'Login failed. Please try again.'
    console.error(err)
  }
}

onMounted(() => {
  //
})

const resetForm = () => {
  formData.value = {
    name: '',
    email: '',
    password: '',
    phone: '',
    address: '',
  }
}
</script>

<style scoped>
</style>
