<template>
  <header class="header">
    <nav>
      <router-link to="/" exact>Home</router-link>
      <router-link to="/drug-development">Drug Development</router-link>
      <router-link to="/analytics">Analytics</router-link>
      <router-link to="/settings">Settings</router-link>
    </nav>
  </header>
</template>

<script setup>
// No script needed for static nav
</script>

<style scoped>
.header {
  background: var(--primary-bg);
  padding: 0.5rem 1rem;
}
nav a {
  margin-right: 1rem;
  color: var(--primary-text);
  text-decoration: none;
}
nav a.router-link-exact-active {
  font-weight: bold;
}
</style>
