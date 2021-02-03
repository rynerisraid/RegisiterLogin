import Vue from 'vue';
import Router from 'vue-router';
import Books from './components/Books'
import Ping from './components/Ping'
import Start from "@/components/Start";


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
      //path：'/'
    {
      path: '/',
      name: 'Start',
      component: Start,
    },

    {
      path: '/Books',
      name: 'Books',
      component: Books,
    },

    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },

  ],
});