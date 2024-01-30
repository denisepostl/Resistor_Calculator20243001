import { createApp } from 'vue';
import App from './App.vue';
import { createI18n } from 'vue-i18n';

const i18n = createI18n({
  locale: 'de',
  messages: {
    de: require('./locales/de.json'),
    en: require('./locales/en.json'),
    fr: require('./locales/fr.json')
  },
});

const app = createApp(App);
app.use(i18n);
app.config.globalProperties.$i18n = i18n; 
app.mount('#app');
