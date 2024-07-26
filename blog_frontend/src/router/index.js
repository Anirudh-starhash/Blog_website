import { createRouter, createWebHistory } from 'vue-router'
import blog_index from '@/components/blog_index.vue'
import blog_about from '@/components/blog_about.vue'
import blog_contact from '@/components/blog_contact.vue'
import blogs from '@/components/blogs.vue'
import change_password from '@/components/change_password.vue'
import blogs_body from '@/components/blogs_body.vue'
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
      path: '/change_password',
      name: 'change_password',
      component: change_password
    },
    {
      path:'/blogs',
      name:'blogs',
      component:blogs
    },
    {
      path:'/blogs/:id',
      name:'blogs_body',
      component:blogs_body
    }
  ]
})

export default router
