<template>
  <div>
    <!-- Users Table -->
    <div class="min-h-[400px] flex flex-col justify-center max-w-4xl mx-auto pt-[100px]" v-if="users.length > 0">
      <h2 class="text-xl font-bold mb-4">Logged in Users List</h2>
      <table class="min-w-full bg-white border border-gray-300">
        <thead class="bg-gray-100">
          <tr>
            <th class="py-2 px-4 border border-gray-300">ID</th>
            <th class="py-2 px-4 border border-gray-300">Name</th>
            <th class="py-2 px-4 border border-gray-300">Email</th>
            <th class="py-2 px-4 border border-gray-300">Phone</th>
            <th class="py-2 px-4 border border-gray-300">Address</th>
            <th class="py-2 px-4 border border-gray-300">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in users" :key="index" class="hover:bg-gray-50">
            <td class="py-2 px-4 border border-gray-300 text-center">{{ user.id }}</td>
            <td class="py-2 px-4 border border-gray-300 text-center">{{ user.name }}</td>
            <td class="py-2 px-4 border border-gray-300 text-center">{{ user.email }}</td>
            <td class="py-2 px-4 border border-gray-300 text-center">{{ user.phone }}</td>
            <td class="py-2 px-4 border border-gray-300 text-center">{{ user.address }}</td>
            <td class="py-2 px-4 border border-gray-300 text-center">
              <button @click="editUser(user.id)" class="text-white bg-blue-500 hover:bg-blue-600 font-medium rounded text-sm px-3 py-1 mr-2">View</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else class="min-h-[660px] flex items-center">
      <div class="hover:shadow-2xl transition all duration-300 ease-in-out mx-auto mt-4 p-4 max-w-md text-center text-red-600 bg-red-100 border border-red-300 rounded-lg">Data not fetched. Something went wrong.</div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const user = localStorage.getItem('user_info')
  if (!user) {
    alert("Please login and see my professional website")
    router.push('/login')
    // window.location.reload()
  }
import useUsers_data from '../Other/composible_api'
const { users, get_all_users } = useUsers_data()

onMounted(async () => {
  await get_all_users()
})

</script>
<style>
</style>
