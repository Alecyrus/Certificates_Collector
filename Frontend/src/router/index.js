import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Home from '@/components/Home'
import CertificatesCollector from '@/components/CertificatesCollector'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'certificates',
      component: Main,
      children: [
        {
          path: '',
          component: Home
        },
        {
          path: 'certificatescollector',
          component: CertificatesCollector
        },
      ]
    },
  ]
})
