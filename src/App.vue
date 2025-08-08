<template>
  <div>
    <nav_bar />
    <ScrollToTopButtonVue />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script setup>
import nav_bar from './components/Nav_and_Footer/nav_bar.vue'
import Footer from './components/Nav_and_Footer/Footer.vue'
import ScrollToTopButtonVue from './components/Other/ScrollToTopButton.vue'
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Sofia;
}
</style>
