<template>
  <footer
    class="bg-white rounded-lg shadow-sm dark:bg-gray-900 m-4 hover:shadow-xl transition-all duration-300 ease-in-out">
    <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <a href="https://www.suvaidyam.com/" target="_blank"
          class="bg-gray-400 border-2 border-gray-200 dark:border-gray-700 px-3 py-1 rounded-lg flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse hover:bg-gray-100 dark:hover:bg-gray-800 hover:shadow-md hover:text-gray-900 dark:hover:text-white transition-all duration-300 ease-in-out">
          <div
            class="h-10 w-10 rounded-full border border-gray-200 dark:border-gray-600 hover:border-gray-300 dark:hover:border-gray-500 relative overflow-hidden bg-gray-50 dark:bg-gray-800 flex items-center justify-center">
            <!-- Logo placeholder - replace with your image -->
            <div class="h-8 w-8 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold">S</div>
          </div>
          <span
            class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white text-gray-800 hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-300">Suvaidyam</span>
        </a>

        <ul
          class="flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400 gap-4 md:gap-6">
          <li v-for="(router, index) in landingPage" :key="index">
            <router-link :to="{ name: router.name }"
              class="hover:text-blue-600 dark:hover:text-blue-400 hover:underline underline-offset-4 transition-colors duration-300 px-1 py-1"
              active-class="text-blue-600 dark:text-blue-400 font-medium">
              {{ router.label }}
            </router-link>
          </li>
        </ul>
      </div>

      <hr class="my-6 border-gray-200 dark:border-gray-700 sm:mx-auto lg:my-8" />

      <div class="flex flex-col items-center sm:flex-row sm:justify-between">
        <span class="text-sm text-gray-500 dark:text-gray-400 text-center sm:text-left mb-4 sm:mb-0">
          © 2023 <a href="https://www.suvaidyam.com/" target="_blank"
            class="hover:text-blue-600 dark:hover:text-blue-400 hover:underline transition-colors duration-300">Suvaidyam</a>.
          All Rights Reserved.
        </span>

        <div class="flex space-x-5 sm:space-x-6">
          <a href="#" class="text-gray-500 hover:text-blue-500 dark:hover:text-blue-400 transition-colors duration-300">
            <span class="sr-only">Facebook</span>
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path fill-rule="evenodd"
                d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
                clip-rule="evenodd" />
            </svg>
          </a>
          <a href="#" class="text-gray-500 hover:text-blue-400 dark:hover:text-blue-300 transition-colors duration-300">
            <span class="sr-only">Twitter</span>
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
            </svg>
          </a>
          <a href="#" class="text-gray-500 hover:text-red-600 dark:hover:text-red-400 transition-colors duration-300">
            <span class="sr-only">YouTube</span>
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path fill-rule="evenodd"
                d="M19.812 5.418c.861.23 1.538.907 1.768 1.768C21.998 8.746 22 12 22 12s0 3.255-.418 4.814a2.504 2.504 0 0 1-1.768 1.768c-1.56.419-7.814.419-7.814.419s-6.255 0-7.814-.419a2.505 2.505 0 0 1-1.768-1.768C2 15.255 2 12 2 12s0-3.255.417-4.814a2.507 2.507 0 0 1 1.768-1.768C5.744 5 11.998 5 11.998 5s6.255 0 7.814.418ZM15.194 12 10 15V9l5.194 3Z"
                clip-rule="evenodd" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { reactive, ref } from 'vue';

const landingPage = reactive([
  { name: 'about', label: 'About' },
  { name: 'privacy', label: 'Privacy Policy' },
  { name: 'listining', label: 'Licensing' },
  { name: 'contact', label: 'Contact' },
])
</script>
<style>
/* Custom underline animation for router links */
.router-link-active {
  position: relative;
}

</style>
