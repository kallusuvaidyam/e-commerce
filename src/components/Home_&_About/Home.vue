<template>
  <div id="home" class="w-full bg-gray-100">
    <!-- Slider Component -->
    <div class="relative">
      <ImageSlider :images="sliderImages" />
      <FormInput v-model="form" :fields="fields" submitText="Submit" @submit="handleSubmit"
        class="absolute top-1/4 md:right-40 z-10 ">
      </FormInput>
    </div>

    <!-- Heading -->
    <h1 class="text-center font-bold text-[22px] mt-6 tracking-widest opacity-[0.7]">
      Here is your Some Content.
    </h1>

    <!-- Filter Dropdown -->
    <select v-model="Select_category"
      class="w-[200px] h-[40px] outline-none bg-gray-200 border border-gray-300 rounded-lg p-2 mt-6 mx-auto block">
      <option>All</option>
      <option>Foods</option>
      <option>Techs</option>
      <option>Books</option>
      <option>Clothes</option>
    </select>

    <!-- Cards Section -->
    <section class="section flex flex-wrap gap-[30px] p-[30px] items-center justify-evenly my-6" id="section">
      <BaseCard v-for="(item, i) in filter_cards" :key="i" v-bind="item" class="card" v-tilt />
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import BaseCard from '../common/BaseCard.vue'
import ImageSlider from '../common/ImageSlider.vue'
import multi_cardsjson from '../../multi_cards.json'
import vTilt from '../common/v-tilt'
import FormInput from '../common/FormInput.vue'

// Register vTilt directive locally
defineOptions({
  directives: {
    tilt: vTilt
  }
})

// Slider images
const sliderImages = [
  'https://images.unsplash.com/photo-1744194210914-0f5b2375645d?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
  'https://images.unsplash.com/photo-1471180625745-944903837c22?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzB8fHRyZWV8ZW58MHx8MHx8fDA%3D',
  'https://plus.unsplash.com/premium_photo-1725408105248-444e6c1a0576?q=80&w=822&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
]

const form = ref({
  email: '',
  password: ''
})

const fields = [
  { name: 'email', label: 'Email', type: 'email', placeholder: 'Your email' },
  { name: 'password', label: 'Password', type: 'password', placeholder: 'Your password' }
]

const handleSubmit = (formData) => {
  alert("Form submitted successfully.")

  formData.email = ''
  formData.password = ''
}

// Card Filter Logic
const Select_category = ref('All')
const multi_cards = ref(multi_cardsjson.multi_cards)

const filter_cards = computed(() =>
  Select_category.value === 'All'
    ? multi_cards.value
    : multi_cards.value.filter(item => item.category === Select_category.value)
)
</script>


<style>
html {
  scroll-behavior: smooth;
}

.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  transform-style: preserve-3d;
}

@media (max-width: 990px) {
  #text {
    width: 100%;
    height: 40px;
    padding: 5px;
  }

  #text p {
    font-size: 15px;
    text-align: left;
  }
}
</style>
