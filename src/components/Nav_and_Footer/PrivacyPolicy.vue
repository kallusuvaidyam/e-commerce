<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 pt-[150px]">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">Privacy Policy</h1>
        <p class="mt-3 text-lg text-gray-500">Last updated: {{ currentDate }}</p>
      </div>

      <!-- Policy Content -->
      <div class="bg-white shadow overflow-hidden sm:rounded-lg">
        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">1. Introduction</h2>
          <p class="mt-2 text-gray-600">
            Welcome to {{ appName }}. We are committed to protecting I'm full stack web developer and your right to privacy. If you have any questions or concerns about this privacy notice, please contact us at
            {{ contactEmail }}.
          </p>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">2. Information We Collect</h2>
          <p class="mt-2 text-gray-600">
            We collect personal information that you voluntarily provide to us when you register on our website, express an interest in obtaining information about us or our products and services, or otherwise when you
            contact us.
          </p>
          <h3 class="mt-4 text-lg font-medium text-gray-700">Personal Information</h3>
          <p class="mt-1 text-gray-600">Kallu kumar, kumarkallu56345@gmail.com, 9065896528</p>
          <h3 class="mt-4 text-lg font-medium text-gray-700">Automatically Collected Information</h3>
          <p class="mt-1 text-gray-600">IP addresses, browser characteristics, operating system details, etc.</p>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">3. How We Use Your Information</h2>
          <ul class="mt-2 list-disc pl-5 space-y-2 text-gray-600">
            <li>To provide and maintain our service</li>
            <li>To notify you about changes to our service</li>
            <li>To allow you to participate in interactive features</li>
            <li>To provide customer support</li>
            <li>To gather analysis or valuable information</li>
            <li>To monitor the usage of our service</li>
            <li>To detect, prevent and address technical issues</li>
          </ul>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">4. Cookies and Tracking Technologies</h2>
          <p class="mt-2 text-gray-600">
            We use cookies and similar tracking technologies to track activity on our website and hold certain information. You can instruct your browser to refuse all cookies or to indicate when a cookie is being sent.
          </p>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">5. Data Security</h2>
          <p class="mt-2 text-gray-600">
            We implement appropriate technical and organizational measures to maintain the safety of your personal information. However, no Internet transmission or electronic storage is ever completely secure.
          </p>
        </div>

        <div class="px-6 py-5 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-800">6. Your Data Protection Rights</h2>
          <p class="mt-2 text-gray-600">Depending on your location, you may have rights including:</p>
          <ul class="mt-2 list-disc pl-5 space-y-2 text-gray-600">
            <li>Access, update or delete your information</li>
            <li>Rectify inaccurate data</li>
            <li>Object to our processing of your data</li>
            <li>Request restriction of processing</li>
            <li>Data portability</li>
            <li>Withdraw consent</li>
          </ul>
        </div>

        <div class="px-6 py-5">
          <h2 class="text-xl font-semibold text-gray-800">7. Changes to This Policy</h2>
          <p class="mt-2 text-gray-600">We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last updated" date.</p>
        </div>

        <!-- Contact Information -->
        <div class="bg-gray-50 px-6 py-4 sm:px-6">
          <h3 class="text-lg font-medium text-gray-900">Contact Us</h3>
          <p class="mt-1 text-gray-600">If you have any questions about this Privacy Policy, please contact us at {{ contactEmail }}.</p>
        </div>
      </div>
    </div>
  </div>
</template>

  <script>
import { ref } from 'vue'

export default {
  setup() {
    const currentDate = ref(
      new Date().toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      })
    )

    // Replace these with your actual app details
    const appName = ref('My e-commorse website')
    const contactEmail = ref('kumarkallu56345@gmail.com')

    return {
      currentDate,
      appName,
      contactEmail,
    }
  },
}
</script>

  <style scoped>
/* You can add custom styles here if needed */
</style>
