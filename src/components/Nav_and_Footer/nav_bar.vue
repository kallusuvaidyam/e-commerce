<template>
  <nav class="bg-gray-500 flex justify-between items-center px-5 py-6 h-[65px] fixed w-full z-19">
    <RouterLink to="/" class="rounded-full p-1 border hover:border-2 transition all duration-300 ease-in-out">
      <img src="../../images/suvaidyam_bg_remove.png" alt="Suvaidyam logo" class="h-[40px] w-[40px] rounded move circle" />
    </RouterLink>

    <div id="setting_bar" class="flex">
      <ul :class="['md:flex gap-5 text-[18px]', menuOpen ? 'show' : '']">
        <li v-for="(item, i) in menuItems" :key="i" class="text-white px-6 py-1 rounded transition-all duration-300 ease-in-out group">
          <RouterLink :to="item.link" @click="menuOpen = false">{{ item.name }}</RouterLink>
          <!-- group parent me hoga tab hi gropu:hover child par work karega -->
          <!-- scale-x-0 :- X-axis mein scale 0 kar deta hai -->
          <span class="block h-[1px] w-full bg-white scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left" :class="[router.path === item.link ? 'scale-x-100' : 'scale-x-0']"> </span>
        </li>
      </ul>
      <div class="md:hidden text-[30px]">
        <i class="fa-solid fa-bars cursor-pointer text-white" @click="menuOpen = !menuOpen"></i>
      </div>
      <!-- Settings Dropdown -->
      <div v-show="user" class="relative cursor-pointer text-white ml-3">
        <i class="fa fa-cog text-xl px-3 py-2 transition-transform duration-300" :class="[featureOpen ? 'rotate-180' : 'rotate-0']" @click="featureOpen = !featureOpen"></i>

        <ul v-show="featureOpen" id="features" class="absolute right-0 top-12 bg-gray-700 rounded shadow-lg z-30 text-left w-40 transition-all duration-300" :class="featureOpen ? 'show' : ''">
          <!-- <li>
            <RouterLink to="/logged-in-users" class="block px-4 py-2 hover:bg-gray-600 text-white">Logged-in Users</RouterLink>
          </li> -->
          <li>
            <button @click="LogOut" class="block px-4 py-2 w-full text-left text-white hover:bg-gray-600">Logout</button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const menuItems = [
  { name: 'Home', link: '/' },
  { name: 'About', link: '/about' },
  { name: 'Services', link: '/services' },
  { name: 'Contact', link: '/contact' },
  { name: 'Blog', link: '/blog' },
]

import { useRoute } from 'vue-router'
const router = useRoute()

const user = localStorage.getItem('user_info')

const menuOpen = ref(false)
const featureOpen = ref(false)

const LogOut = () => {
  const isConfirmed = window.confirm('Are you sure?')
  if (isConfirmed) {
    localStorage.removeItem('user_info')
    window.location.reload()
    router.push('/login')
  }
}
</script>

<style>
/* ----- Mobile Menu Styles (max-width: 768px) ----- */
@media (max-width: 768px) {
  nav ul {
    position: absolute;
    top: 65px;
    left: 0;
    z-index: 20;
    width: 100%;
    text-align: center;
    background: #60656e;

    transform: translateY(-70px);
    opacity: 0;
    pointer-events: none;

    transition: transform 0.3s ease, opacity 0.3s ease;
  }

  nav ul.show {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }

  nav ul li:hover {
    background-color: rgb(63, 70, 70);
  }

  nav ul li span {
    display: none !important;
  }

  #features {
    left: -120px;
  }
}

/* ----- Logo Rotation Animation ----- */
@keyframes round {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.move {
  animation: round 8s linear infinite;
}

.move:hover {
  animation-play-state: paused;
}

ul[style] {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
