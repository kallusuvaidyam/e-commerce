<template>
  <div class="p-6">
    <FormInput v-model="form" :fields="fields" submitText="Send Message" @submit="handleSubmit">
      <template #extra>
        <p class="text-sm text-gray-500">We’ll get back to you within 24 hours.</p>
      </template>
    </FormInput>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import FormInput from '../common/FormInput.vue'
const form = ref({})

const fields = [
  { name: 'name', label: 'Name', type: 'text', placeholder: 'Your name' },
  { name: 'email', label: 'Email', type: 'email', placeholder: 'Your email' },
  { name: 'message', label: 'Message', type: 'text', placeholder: 'Your message' }
]

const handleSubmit = (formData) => {
  console.log('Form submitted:', formData)
  // send to API or do something
}
</script>
