import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: () => import('@/components/Home_&_About/Home.vue') },
    { path: '/about', name: 'about', component: () => import('@/components/Home_&_About/about.vue'), meta: { requiresAuth: true } },
    { path: '/contact', name: 'contact', component: () => import('@/components/Home_&_About/Contect.vue') },
    { path: '/nav_bar', name: 'nav_bar', component: () => import('@/components/Nav_and_Footer/nav_bar.vue') },
    { path: '/footer', name: 'footer', component: () => import('@/components/Nav_and_Footer/Footer.vue') },
    { path: '/blog', name: 'blog', component: () => import('@/components/Nav_and_Footer/Blog.vue'), meta: { requiresAuth: true } },
    { path: '/privacy', name: 'privacy', component: () => import('@/components/Nav_and_Footer/PrivacyPolicy.vue') },
    { path: '/listining', name: 'listining', component: () => import('@/components/Nav_and_Footer/listining.vue') },
    { path: '/login', name: 'login', component: () => import('@/components/Jump_buttons/LogIn.vue'), meta: { guestOnly: true } },
    { path: '/learn_more', name: 'learn_more', component: () => import('@/components/Jump_buttons/Learn_more.vue') },
    { path: '/services', name: 'services', component: () => import('@/components/Other/Services.vue'), meta: { requiresAuth: true } },
    {
      path: '/:pathMatch(.*)*', // catch-all for 404
      name: 'NotFound',
      component: () => import('../NotFound.vue'),
    },
  ],
})

// router.beforeEach((to, from, next) => {
//   const isAuthenticated = !!localStorage.getItem('user_info') // !!: Double NOT operator — iska use isliye kiya jaata hai taaki koi bhi value ko true/false me convert kiya jaa sake.

//   if (to.meta.requiresAuth && !isAuthenticated) {
//     alert('Please login and see my professional website')
//     next({ name: 'login' })
//   } else if (to.meta.guestOnly && isAuthenticated) {
//     next("/")
//   } else {
//     next()
//   }
// })

export default router
