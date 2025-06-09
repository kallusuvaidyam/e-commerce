<template>
  <footer class="bg-white rounded-lg shadow-sm dark:bg-gray-900 m-4 hover:shadow-xl transition all duration-300 ease">
    <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <a href="https://www.suvaidyam.com/" target="_blank" class="border-2 px-3 py-1 rounded flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse hover:bg-[#6B7280] hover:shadow-xl hover:text-white transition all duration-300 ease">
          <div class="h-[40px] w-[40px] rounded-full border hover:border-2 relative">
            <img src="../../images/suvaidyam_bg_remove.png" id="move" class="h-8 absolute left-1 top-1" alt="Suvaidyam Logo" />
          </div>
          <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Suvaidyam</span>
        </a>
        <ul class="flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400">
          <li>
            <router-link :to="{name: 'about'}" class="hover:underline me-4 md:me-6">About</router-link>
          </li>
          <li>
            <router-link :to="{name: 'privacy'}" class="hover:underline me-4 md:me-6">Privacy Policy</router-link>
          </li>
          <li>
            <router-link :to="{name: 'listining'}" class="hover:underline me-4 md:me-6">Licensing</router-link>
          </li>
          <li>
            <router-link :to="{name: 'contact'}" class="hover:underline me-4 md:me-6">Contact</router-link>
          </li>
        </ul>
      </div>
      <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
      <span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">
        © 2023
        <a href="https://www.suvaidyam.com/" target="_blank" class="hover:underline"> Suvaidyam </a>.
        All Rights Reserved.
      </span>
    </div>
  </footer>
</template>

<script setup>
// कोई extra JavaScript की जरूरत नहीं है क्योंकि यह purely static component है
</script>
<style>
@keyframes round {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

#move {
  animation: round 8s linear infinite;
}

#move:hover {
  animation-play-state: paused;
}
</style>
