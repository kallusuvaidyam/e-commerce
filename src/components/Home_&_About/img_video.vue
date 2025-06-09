<template>
  <div class="mt-[20px]">
    <div class="p-4 max-w-2xl mx-auto">
    <h2 class="text-xl font-bold mb-4">Instagram Video Embed</h2>

    <!-- Instagram Embed -->
    <div ref="instaEmbed" class="mb-4">
      <blockquote
        class="instagram-media"
        data-instgrm-permalink="https://www.instagram.com/p/DJW-75BIz9I/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
        data-instgrm-version="14"
        style="background:#FFF; border:0; margin:0 auto; max-width:540px; width:99%;"
      ></blockquote>
    </div>
  </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
const instaEmbed = ref(null)

onMounted(() => {
  // Instagram embed script load
  if (!window.instgrm) {
    const script = document.createElement('script')
    script.setAttribute('src', 'https://www.instagram.com/embed.js')
    script.setAttribute('async', '')
    document.body.appendChild(script)
  } else {
    // Agar pehle se load hai
    window.instgrm.Embeds.process()
  }
})
</script>

<style>

</style>
