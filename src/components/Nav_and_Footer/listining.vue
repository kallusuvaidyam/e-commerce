<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 pt-[100px]">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
          Licensing Information
        </h1>
        <p class="mt-3 text-lg text-gray-500">
          Last updated: {{ currentDate }}
        </p>
      </div>

      <!-- Licensing Content -->
      <div class="bg-white shadow overflow-hidden sm:rounded-lg">
        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">1. Software License</h2>
          <p class="mt-2 text-gray-600">
            {{ appName }} is licensed under the {{ licenseType }} unless otherwise noted.
            This license governs your use of the software and associated documentation.
          </p>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">2. Permissions</h2>
          <ul class="mt-2 list-disc pl-5 space-y-2 text-gray-600">
            <li v-for="permission in permissions" :key="permission">
              {{ permission }}
            </li>
          </ul>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">3. Restrictions</h2>
          <ul class="mt-2 list-disc pl-5 space-y-2 text-gray-600">
            <li v-for="restriction in restrictions" :key="restriction">
              {{ restriction }}
            </li>
          </ul>
          <p class="mt-4 text-gray-600">
            Violation of these terms will result in immediate termination of your license.
          </p>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">4. Third-Party Licenses</h2>
          <p class="mt-2 text-gray-600">
            This software includes components from third parties that are subject to their own licenses:
          </p>
          <div class="mt-4 space-y-4">
            <div v-for="(license, lib) in thirdPartyLicenses" :key="lib" class="pl-4 border-l-4 border-blue-200">
              <h3 class="text-lg font-medium text-gray-700">{{ lib }}</h3>
              <p class="mt-1 text-gray-600">{{ license }}</p>
            </div>
          </div>
        </div>

        <!-- Contact Information -->
        <div class="bg-gray-50 px-6 py-4 sm:px-6">
          <h3 class="text-lg font-medium text-gray-900">License Questions?</h3>
          <p class="mt-1 text-gray-600">
            If you have any questions about licensing, please contact us at {{ contactEmail }}.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import multi_cards from '../../multi_cards.json'
const permissions = multi_cards.permissions
const restrictions = multi_cards.restrictions
const thirdPartyLicenses = multi_cards.thirdPartyLicenses

const currentDate = ref(new Date().toLocaleDateString('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric'
}));

// Customize these values for your application
const appName = ref('My e-commorse website');
const contactEmail = ref('kumarkallu56345@gmail.com');
const licenseType = ref('MIT License');
const licenseUrl = ref('https://opensource.org/licenses/MIT');

</script>

<style scoped>
/* Custom styles if needed */
</style>
