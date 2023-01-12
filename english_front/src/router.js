import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: () => import('./pages/WordsPage')
    },
    // {
    //     path: '/debtor',
    //     component: () => import('./pages/DebtorPage')
    // },
    // {
    //     path: '/payments',
    //     component: () => import('./pages/PaymentsPage')
    // },
    // {
    //     path: '/mail',
    //     component: () => import('./pages/MailPage')
    // },
    // {
    //     path: '/library',
    //     component: () => import('./pages/LibraryPage')
    // },
    // {
    //     path: '/statistics',
    //     component: () => import('./pages/StatisicsPage')
    // },
]

export default new VueRouter({
    mode: 'history',
    routes
})