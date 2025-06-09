<template>
  <div id="home" class="w-full bg-gray-100">
    <!-- Slider Image Section -->
    <section id="slider" class="slider w-full h-[500px] bg-gray-300 flex items-center justify-center pt-[65px]">
      <div class="image-container w-full h-full relative">
        <!-- Left Navigation Button -->
        <button class="animate__animated animate__fadeIn absolute w-[55px] left-4 top-1/2 transform -translate-y-1/2 z-10 bg-black bg-opacity-50 text-white p-2 rounded-full hover:bg-opacity-75" @click="prevImage">
          <i class="fa fa-chevron-left mr-[3px] text-[36px]"></i>
        </button>

        <!-- Right Navigation Button -->
        <button class="animate__animated animate__fadeIn absolute w-[55px] right-4 top-1/2 transform -translate-y-1/2 z-10 bg-black bg-opacity-50 text-white p-2 rounded-full hover:bg-opacity-75" @click="nextImage">
          <i class="fa fa-chevron-right ml-[3px] text-[36px]"></i>
        </button>

        <!-- Slider Images -->
        <div class="w-full overflow-hidden">
          <img src="../../images/teamwork1.jpg" class="active absolute w-full h-full" />
          <img src="../../images/teamwork2.jpg" class="absolute w-full h-full" />
          <img src="../../images/teamwork3.jpg" class="absolute w-full h-full" />
        </div>

        <!-- Slider Text Content -->
        <div class="z-[2] absolute left-1/2 transform -translate-x-1/2 w-1/2 text-center" id="text">
          <h1 class="animate__animated animate__slideInLeft font-bold text-3xl text-white font-serif mt-9">Welcome to our website</h1>
          <p class="text-center text-white">
            I'm Kallu, a passionate full-stack web developer skilled in building fast, responsive, and user-friendly websites. I work with modern technologies like HTML, CSS, JavaScript, Vue.js, Python (Flask), and SQL
            to create clean and scalable web solutions. From landing pages to full web apps with features like login, form validation, and CRUD, I deliver polished, mobile-ready designs with solid functionality. I focus
            on performance, clean code, and client satisfaction. Let’s turn your ideas into powerful digital experiences.
          </p>

          <router-link :to="{ name: 'login' }">
            <button
              v-if="!isLoggedIn"
              class="mt-6 opacity-[0.7] text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
              data-intro="Go to Login Page"
            >
              Login
            </button>
          </router-link>
          <router-link :to="{ path: 'learn_more' }">
            <button class="ml-3 px-4 py-2 bg-black text-white rounded-lg shadow hover:opacity-[0.7] transition mt-3 duration-300">Learn more</button>
          </router-link>
        </div>
      </div>
    </section>

    <h1 class="text-center font-bold text-[22px] mt-6 tracking-widest opacity-[0.7]">Here is your Some Content.</h1>
    <select name="opt" id="opt" v-model="Select_category" class="w-[200px] h-[40px] outline-none bg-gray-200 border border-gray-300 rounded-lg p-2 mt-6 mx-auto block">
      <option>All</option>
      <option>Foods</option>
      <option>Techs</option>
      <option>Books</option>
      <option>Clothes</option>
    </select>

    <!-- Cards Section -->
    <section class="section flex flex-wrap gap-[30px] p-[30px] items-center justify-evenly my-6" id="section">
      <div :class="`${item.div_class}`" v-for="(item, index) in filter_cards" :key="index">
        <div class="overflow-hidden w-full h-[220px]">
          <a href="#" class=""><img :class="`${item.img_class}`" :src="item.image" alt="Ply bord" /></a>
        </div>
        <div class="p-5">
          <a href="#"
            ><h5 :class="`${item.h5_class}`">{{ item.title }}</h5></a
          >
          <p :class="[item.p_class]">{{ item.subtitle }}</p>
          <p :class="`${item.p_class}`">{{ item.description }}</p>
          <a href="#" :class="`${item.a_class}`">{{ item.buttonText }}</a>
        </div>
      </div>
    </section>

    <!-- Moving img -->
    <clousre />
  </div>
</template>

<script setup>
import clousre from '../Other/clousre.vue'
import { computed, onMounted, ref } from 'vue'

// foods
import Food1 from '../../images/food1.jpg'
import Food2 from '../../images/food2.jpg'

// Techs
import Keyboard from '../../images/keybord.jpg'
import Mouse from '../../images/mouse.jpeg'
import Ofice from '../../images/office.jpg'

// books
import Book1 from '../../images/book1.jpg'

// clothes
import Clothe from '../../images/clothes1.jpg'

// import { useRoute } from 'vue-router' // Useful when you want to read the current route’s params, query, name, etc.
// import { useRouter } from 'vue-router' // Useful when you want to navigate to another route or manipulate the router.
// const router = useRouter()

const Select_category = ref('All')

const multi_cards = ref([
  {
    image: Food1,
    title: 'Food',
    subtitle: 'Creative & modern visuals',
    description: 'Food is essential for life, giving energy, health, and happiness.',
    buttonText: 'Buy Now',
    category: 'Foods',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
  {
    image: Keyboard,
    title: 'Keyboard',
    subtitle: 'Creative & modern visuals',
    description: 'The quality of the keyboard affects typing speed, comfort and remoteness.',
    buttonText: 'Buy Now',
    category: 'Techs',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
  {
    image: Food2,
    title: 'Food',
    subtitle: 'Creative & modern visuals',
    description: 'Food is essential for life, giving energy, health, and happiness.',
    buttonText: 'Buy Now',
    category: 'Foods',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
  {
    image: Clothe,
    title: 'Clothe',
    subtitle: 'Creative & modern visuals',
    description: 'Clothes protect the body, express style, and reflect culture.',
    buttonText: 'Buy Now',
    category: 'Clothes',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
  {
    image: Book1,
    title: 'Book1',
    subtitle: 'Creative & modern visuals',
    description: 'Books provide knowledge, spark imagination, and preserve stories and history.',
    buttonText: 'Buy Now',
    category: 'Books',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
  {
    image: Mouse,
    title: 'Mouse',
    subtitle: 'Creative & modern visuals',
    description: 'A mouse is a device that controls the computer cursor easily.',
    buttonText: 'Buy Now',
    category: 'Techs',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
  {
    image: Ofice,
    title: 'Office',
    subtitle: 'Creative & modern visuals',
    description: 'An office is a place where people work, plan, and collaborate.',
    buttonText: 'Buy Now',
    category: 'Techs',
    link: 'kalluweb.vercel.app',
    div_class: 'card hover:shadow-lg transition-all duration-300 ease-in-out max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700',
    img_class: 'card-image rounded-t-lg w-full hover:scale-[1.1] transition-all duration-300 ease-in-out',
    h5_class: 'font-serif text-[25px] opacity-[0.7] mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white',
    p_class: 'mb-3 font-normal text-gray-700 dark:text-gray-400 font-serif text-[16px] opacity-[0.7]',
    a_class: 'inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:outline-none dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
  },
])

const filter_cards = computed(() => {
  return Select_category.value === 'All' ? multi_cards.value : multi_cards.value.filter((item) => item.category === Select_category.value)
})

const currentIndex = ref(0)
let intervalId = null

const nextImage = () => {
  const images = document.querySelectorAll('.image-container img')
  images[currentIndex.value].classList.remove('active')
  currentIndex.value = (currentIndex.value + 1) % images.length
  images[currentIndex.value].classList.add('active')
  resetInterval()
}

const prevImage = () => {
  const images = document.querySelectorAll('.image-container img')
  images[currentIndex.value].classList.remove('active')
  currentIndex.value = (currentIndex.value - 1 + images.length) % images.length
  images[currentIndex.value].classList.add('active')
  resetInterval()
}

const resetInterval = () => {
  if (intervalId) {
    clearInterval(intervalId)
  }
  intervalId = setInterval(nextImage, 3000)
}

onMounted(() => {
  // Initialize slider
  const images = document.querySelectorAll('.image-container img')
  if (images.length > 0) {
    images[0].classList.add('active')
    resetInterval()
  }

  // Card tilt effect
  const cards = document.querySelectorAll('.card')
  cards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const box = card.getBoundingClientRect()
      const x = e.clientX - box.left
      const y = e.clientY - box.top

      const centerX = box.width / 2
      const centerY = box.height / 2

      const rotateX = -(y - centerY) / 20
      const rotateY = (x - centerX) / 20

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`
    })

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)'
    })
  })
})
// let user = localStorage.getItem("user_info")
// console.log(user);

const isLoggedIn = computed(() => {
  return !!localStorage.getItem('user_info')
})
</script>

<style>
html {
  scroll-behavior: smooth;
}

.image-container img {
  opacity: 0;
  transition: opacity 1s ease;
  object-fit: cover;
}
.image-container img.active {
  opacity: 1;
  z-index: 1;
}
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  transform-style: preserve-3d;
}

.card-image {
  transition: transform 0.3s ease;
}

.image-container button {
  transition: background-opacity 0.3s ease;
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
