<template>
  <div id="about" class="bg-gray-10">
    <section class="min-h-auto py-16 px-6 md:px-24 bg-gray-100 dark:bg-gray-900 hover:shadow-xl transition-all duration-300 ease font-sans">
      <div class="max-w-5xl mx-auto">
        <!-- Heading -->
        <div class="text-center mb-12">
          <h1 class="text-5xl font-bold text-gray-800 dark:text-white my-4">About Me</h1>
          <p class="text-lg text-gray-500 dark:text-gray-300 max-w-2xl mx-auto">
            Empowering businesses with clean, fast, and modern web solutions.
          </p>
        </div>

        <!-- Content Grid -->
        <div class="grid md:grid-cols-2 gap-12 items-start">
          <!-- Left: Who I Am -->
          <div>
            <h2 class="text-2xl font-semibold text-gray-800 dark:text-white mb-3">Who I Am</h2>
            <p class="text-gray-600 dark:text-gray-300 mb-4">
              I'm <span class="font-semibold text-indigo-600 dark:text-indigo-400">Kallu</span>, a full-stack web developer with 3+ years of experience.
              I create scalable, accessible, and performance-driven solutions.
            </p>
            <p class="text-gray-600 dark:text-gray-300">
              I believe in building things that not only work but also create value for users and clients.
            </p>
          </div>

          <!-- Right: Tech Stack -->
          <div>
            <h2 class="text-2xl font-semibold text-gray-800 dark:text-white mb-3">Tech Stack</h2>
            <ul class="space-y-2 text-gray-700 dark:text-gray-300">
              <li>🔹 Frontend: Vue.js, Tailwind CSS, JavaScript, HTML5</li>
              <li>🔹 Backend: Flask (Python), Node.js</li>
              <li>🔹 Database: MySQL, MongoDB</li>
              <li>🔹 Tools: Git, Postman, VS Code</li>
            </ul>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="mt-16 text-center">
          <h2 class="text-2xl font-semibold text-gray-800 dark:text-white mb-2">Ready to Collaborate?</h2>
          <p class="text-gray-600 dark:text-gray-300 mb-6">
            Let’s build something amazing together. Feel free to reach out!
          </p>
          <router-link to="/contact">
            <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-8 py-3 rounded-full shadow-lg transition duration-300">
              Contact Me
            </button>
          </router-link>
        </div>
      </div>
    </section>

    <img_video />
  </div>
</template>

<script setup>
import img_video from './img_video.vue'
</script>

<style>
@media (max-width: 768px) {
  #toggle {
    width: 90%;
  }
  #title,
  #params {
    font-size: 15px;
  }
}
</style>
