<template>
  <form @submit.prevent="handleSubmit" class="space-y-4 p-4 bg-white rounded-xl shadow-md w-full max-w-md mx-auto">
    <div v-for="(field, index) in fields" :key="index" class="w-full">
      <label :for="field.name" class="block text-sm sm:text-base font-medium text-gray-700 mb-1">{{ field.label
        }}</label>
      <input v-model="formData[field.name]" :type="field.type" :id="field.name" :name="field.name"
        :placeholder="field.placeholder || ''"
        class="w-full px-3 py-2 sm:px-4 sm:py-2 text-sm sm:text-base border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
        :required="field.required !== false" />
    </div>

    <slot name="extra"></slot> <!-- Optional extra slot -->

    <button type="submit"
      class="w-full py-2 px-4 text-sm sm:text-base bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition">
      {{ submitText }}
    </button>
  </form>
</template>

<script setup>
import { reactive, watch } from 'vue'

const props = defineProps({
  fields: {
    type: Array,
    required: true,
    // Example: [{ name: 'email', label: 'Email', type: 'email', placeholder: 'Enter email' }]
  },
  modelValue: {
    type: Object,
    default: () => ({})
  },
  submitText: {
    type: String,
    default: 'Submit'
  }
})

const emit = defineEmits(['update:modelValue', 'submit'])

const formData = reactive({ ...props.modelValue })

watch(formData, () => {
  emit('update:modelValue', formData)
}, { deep: true })

const handleSubmit = () => {
  emit('submit', formData)
}
</script>
