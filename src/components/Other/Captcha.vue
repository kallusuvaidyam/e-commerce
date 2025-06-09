<template>
  <div class="flex items-center justify-center h-screen bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-md text-center">
      <h2 class="text-xl font-semibold mb-4">Verify You're Human</h2>
      <canvas ref="canvasRef" width="200" height="50" class="my-2 border border-gray-300 bg-gray-200"></canvas>
      <button
        @click="generateCaptcha"
        class="mt-2 mb-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Reload CAPTCHA
      </button>
      <input
        v-model="userInput"
        type="text"
        placeholder="Enter CAPTCHA"
        class="w-48 p-2 mb-2 border border-gray-300 rounded outline-none"
      />
      <div :class="['text-sm mt-2', isCorrect === true ? 'text-green-600' : isCorrect === false ? 'text-red-600' : '']">
        {{ resultMessage }}
      </div>
      <button
        @click="validateCaptcha"
        class="mt-3 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const canvasRef = ref(null);
const generatedCaptcha = ref('');
const userInput = ref('');
const resultMessage = ref('');
const isCorrect = ref(null);

function generateCaptcha() {
  const canvas = canvasRef.value;
  const ctx = canvas.getContext('2d');
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  generatedCaptcha.value = '';

  // Generate 6-character string
  for (let i = 0; i < 6; i++) {
    generatedCaptcha.value += chars.charAt(Math.floor(Math.random() * chars.length));
  }

  // Clear and draw
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.font = '30px Arial';
  ctx.fillStyle = '#000';
  ctx.setTransform(1, 0, 0, 1, 0, 0);

  for (let i = 0; i < generatedCaptcha.value.length; i++) {
    const angle = (Math.random() - 0.5) * 0.4;
    ctx.save();
    ctx.translate(30 * i + 10, 35);
    ctx.rotate(angle);
    ctx.fillText(generatedCaptcha.value[i], 0, 0);
    ctx.restore();
  }

  // Draw noise
  for (let i = 0; i < 5; i++) {
    ctx.strokeStyle = '#888';
    ctx.beginPath();
    ctx.moveTo(Math.random() * canvas.width, Math.random() * canvas.height);
    ctx.lineTo(Math.random() * canvas.width, Math.random() * canvas.height);
    ctx.stroke();
  }
}

function validateCaptcha() {
  if (userInput.value === generatedCaptcha.value) {
    resultMessage.value = '✅ CAPTCHA Verified!';
    isCorrect.value = true;
  } else {
    resultMessage.value = '❌ Incorrect CAPTCHA. Try again.';
    isCorrect.value = false;
  }
}

onMounted(generateCaptcha);
</script>

<style scoped>
canvas {
  image-rendering: pixelated;
}
</style>
