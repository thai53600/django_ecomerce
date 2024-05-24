<template>
    <!-- form wrapper -->
    <div class="container py-16">
      <div class="max-w-lg mx-auto shadow px-6 py-7 rounded overflow-hidden">
        ...
        <form @submit.prevent="handleSubmit">
          <div>
            <label for="username">Username</label>
            <input type="text" id="username" class="input-box w-full" placeholder="John Doe" required v-model="username" />
          </div>
          <div>
            <label for="email">Email</label>
            <input type="email" id="email" class="input-box w-full" placeholder="example@mail.com" required v-model="email" />
          </div>
          <div>
            <label for="password">Password</label>
            <input type="password" id="password" class="input-box w-full" placeholder="type password" required v-model="password" />
          </div>
          <button type="submit" class="block w-full py-2 text-center text-white bg-primary border border-primary rounded hover:bg-transparent hover:text-primary transition uppercase font-roboto font-medium">
            Create Account
          </button>
        </form>
      </div>
    </div>
    <!-- form wrapper end -->
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import AuthAPI from '@/api/auth.api'
  
  const username = ref('')
  const email = ref('')
  const password = ref('')
  
  const handleSubmit = async () => {
    try {
      const response = await AuthAPI.logup({
        email: email.value,
        username: username.value,
        password: password.value
      })
      console.log('Registration successful:', response)
      // Xử lý sau khi đăng ký thành công, ví dụ: chuyển hướng đến trang khác
    } catch (error) {
      console.error('Registration failed:', error)
      // Xử lý lỗi đăng ký, ví dụ: hiển thị thông báo lỗi
    }
  }
  </script>
  
