import { createRouter, createWebHistory } from 'vue-router'
import blog_index from '@/components/blog_index.vue'
import blog_about from '@/components/blog_about.vue'
import blog_contact from '@/components/blog_contact.vue'
import login_component from '@/components/login_component.vue'
import register_component from '@/components/register_component.vue'
import change_password from '@/components/change_password.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'blog_index',
      component: blog_index
    },
    {
      path: '/about',
      name: 'blog_about',
      component: blog_about
    },
    {
      path: '/contact',
      name: 'blog_contact',
      component: blog_contact
    },
    {
      path: '/login',
      name: 'login_component',
      component: login_component
    },
    {
      path: '/register',
      name: 'register_component',
      component: register_component
    },
    {
      path: '/change_password',
      name: 'change_password',
      component: change_password
    },
  ]
})

export default router
