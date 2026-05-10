<template>
  <div id="app">
    <Header />
    <router-view class="view" />
    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.view {
  flex: 1;
  padding: 1rem;
}
</style>
