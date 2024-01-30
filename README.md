# R-Calculator

## Installation von Vue
```python 
npm install -g @vue/cli # Vue Cli global installieren

vue create r_calculator_frontend # Neues Vue-Projekt erstellen

cd r_calculator_frontend # Zum Projektverzeichnis wechseln
```

## Installation von i18n
i18n ist eine Abkürzung für "Internationalization", und es bezieht sich auf die Anpassung von Software, Websites oder Anwendungen, um sie leicht in verschiedene Sprachen und kulturelle Kontexte übersetzen und anpassen zu können.

```python 
npm install vue-i18n
```

Jetzt können in einem neuen Ordner Sprachdateien erstellt werden. Um sie im App.vue zu verwenden, muss die main.js-Datei entsprechend angepasst werden:

```python
// Die benötigten Vue- und i18n-Module importieren
import { createApp } from 'vue';
import App from './App.vue';
import { createI18n } from 'vue-i18n';

// Eine neue i18n-Instanz mit den gewünschten Sprachen und Pfaden zu den Sprachdateien erstellen
const i18n = createI18n({
  locale: 'de',
  messages: {
    de: require('./locales/de.json'),
    en: require('./locales/en.json'),
    fr: require('./locales/fr.json')
  },
});

// Vue-App erstellen und die i18n-Instanz hinzufügen
const app = createApp(App);
app.use(i18n);
app.config.globalProperties.$i18n = i18n; 
app.mount('#app');

```