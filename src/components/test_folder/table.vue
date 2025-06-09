<template>
  <div class="p-4 max-w-3xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">Data Table with Filter & Row Count</h1>

    <!-- 🔍 Filter Inputs -->
    <div class="flex gap-4 mb-2">
      <select v-model="searchBy" class="border px-3 py-2 rounded">
        <option value="name">Search by Name</option>
        <option value="id">Search by ID</option>
      </select>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search..."
        class="border px-3 py-2 rounded w-full"
      />
    </div>

    <!-- 📢 Row Count Info -->
    <p class="text-sm text-gray-600 mb-3">
      Showing {{ visibleStart }} to {{ visibleEnd }} of {{ filteredData.length }} entries
    </p>

    <!-- 📋 Table -->
    <table class="min-w-full border border-gray-300">
      <thead class="bg-gray-100">
        <tr>
          <th class="py-2 px-4 border">Index</th>
          <th class="py-2 px-4 border">ID</th>
          <th class="py-2 px-4 border">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, index) in filteredVisibleData"
          :key="item.id"
          class="hover:bg-gray-50"
        >
          <td class="py-2 px-4 border">{{ index }}</td>
          <td class="py-2 px-4 border">{{ item.id }}</td>
          <td class="py-2 px-4 border">{{ item.name }}</td>
        </tr>
        <tr v-if="filteredVisibleData.length === 0">
          <td colspan="3" class="py-3 px-4 text-center text-gray-500">No matching data found.</td>
        </tr>
      </tbody>
    </table>

    <!-- 🔘 Show All Button -->
    <div class="mt-4">
      <button
        v-if="!showAll"
        @click="showAll = true"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Show All
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const allData = ref([
  { id: 1, name: 'Amit' },
  { id: 2, name: 'Priya' },
  { id: 3, name: 'Rohan' },
  { id: 4, name: 'Sita' },
  { id: 5, name: 'Mohan' },
  { id: 6, name: 'Nina' }
])

const showAll = ref(false)
const searchBy = ref('name')
const searchQuery = ref('')

// ✅ Filtered Data
const filteredData = computed(() => {
  if (!searchQuery.value.trim()) return allData.value
  return allData.value.filter(item =>
    item[searchBy.value].toString().toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

// ✅ Visible Data
const filteredVisibleData = computed(() =>
  showAll.value ? filteredData.value : filteredData.value.slice(0, 3)
)

// ✅ Count Range
const visibleStart = computed(() => (filteredVisibleData.value.length > 0 ? 0 : 0))
const visibleEnd = computed(() => filteredVisibleData.value.length - 1)
</script>
