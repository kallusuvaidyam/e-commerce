<template>
  <div id="scroll_btn" class="relative">
    <i
    v-show="showScrollToTop"
    @click="scrollToTop"
    class="fa fa-arrow-up text-[20px] text-white bg-green-600 p-[10px] rounded-[50%] fixed right-[35px] bottom-[35px] z-50 cursor-pointer hover:bg-green-700 transition"
    />
  </div>
</template>

<script setup>
import { onUnmounted, onMounted, ref } from "vue";

const showScrollToTop = ref(false)

const handelScroll = () => {
  showScrollToTop.value = window.pageYOffset > 300
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  })
}

onMounted(() => {
  window.addEventListener("scroll", handelScroll)
})

onUnmounted(() => {
  window.removeEventListener("scroll", handelScroll)
})
</script>

<style>

</style>
