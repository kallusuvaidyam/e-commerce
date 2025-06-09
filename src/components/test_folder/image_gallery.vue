<template>
  <div class="flex flex-wrap justify-evenly gap-5">
    <div
      v-for="(item, i) in multi_cards"
      :key="i"
      class="relative w-[400px] h-[300px] overflow-hidden group"
    >
      <img
        :src="item.img"
        alt=""
        class="w-full h-full object-cover transition duration-300 ease-in-out group-hover:grayscale-[90%] cursor-pointer"
        @click="openModal(item.img)"
      />
      <i
        :class="item.icon"
        class="absolute top-1/2 left-1/2 text-white text-[28px] opacity-70 hidden group-hover:block transform -translate-x-1/2 -translate-y-1/2 transition-all duration-300 ease-in-out"
      ></i>
      <p v-html="item.Discription" class="absolute bottom-2 left-2 text-white text-sm bg-black/50 px-2 py-1 rounded"></p>
    </div>
  </div>

  <!-- Modal -->
  <div
    v-if="showModal"
    class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50"
    @click.self="closeModal"
  >
    <div class="max-w-3xl w-full relative">
      <button
        @click="closeModal"
        class="absolute top-2 right-2 text-white text-2xl font-bold z-10"
      >
        &times;
      </button>
      <img :src="modalImage" alt="Enlarged" class="w-full h-auto rounded shadow-lg" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import img from '../../images/amaresh.jpeg'

const iconClass = 'fa fa-search-plus'
const para = '<p>This is my image</p>'

const multi_cards = ref(
  Array.from({ length: 10 }, () => ({
    img,
    icon: iconClass,
    Discription: para
  }))
)

// Modal logic
const showModal = ref(false)
const modalImage = ref(null)

function openModal(imageSrc) {
  modalImage.value = imageSrc
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}
</script>
