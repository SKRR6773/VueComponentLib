import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/bootstrap-icons/font/bootstrap-icons.min.css';

import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import routes from './routes';


createApp(App).use(routes).mount('#app')