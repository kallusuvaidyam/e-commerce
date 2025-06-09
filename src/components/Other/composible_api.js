import { ref } from "vue";
import axios from "axios";

export default function useUsers_data() {
  // let url = 'http://localhost:8080/users/'
  // let url = 'http://localhost:5000/'
  let url = 'https://flask-backend-35vq.onrender.com'
  let users = ref([])
  let err = ref(null)

  // Add user
  const add_user = async (user_data) => {
    users.value = []
    err.value = null

    try {
      const config = {
        method: 'POST',
        url: url + 'add_user/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: JSON.stringify(user_data),
      }
      const response = await axios(config)
      users.value = response.data
    } catch (error) {
      err.value = `Error fetching users: ${error.message}`
    }
  }

  // Contacted user
  const Contacted_user = async (contacted_users_data) => {
    users.value = []
    err.value = null

    try {
      const config = {
        method: 'POST',
        url: url + 'contacted_users',
        headers: {
          'Content-Type': 'application/json',
        },
        data: JSON.stringify(contacted_users_data),
      }
      const response = await axios(config)
      users.value = response.data
    } catch (error) {
      err.value = `Error fetching users: ${error.message}`
    }
  }

  return { users, err, add_user, Contacted_user }
}
