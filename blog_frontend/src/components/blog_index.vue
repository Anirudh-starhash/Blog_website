<template>
    <div class="blog-index">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
      <header class="header">
        <nav class="nav">
          <router-link to="/" class="nav-item">HOME</router-link>
          <router-link to="/about" class="nav-item">ABOUT</router-link>
          <router-link to="/contact" class="nav-item">CONTACT</router-link>
          <router-link to="/blogs" class="nav-item">BLOGS</router-link>
          <router-link to="/register" class="nav-item">SIGN-UP</router-link>
          <router-link to="/login" class="nav-item">SIGN-IN</router-link>
        </nav>
      </header>
  
      <main class="content">
        <h1>Welcome to the Blog Website</h1>
        <p>
          This is a platform where you can read, edit, and delete your own blogs.
          You can also like, share, and comment on other users' blogs.
        </p>
        <p>
          Admins have special powers to delete users, edit certain users' blogs, and perform other CRUD operations.
        </p>
      </main>
  
      <footer class="footer">
        <p>&copy; 2024 Ani's Blog Website. All rights reserved.</p>
      </footer>
     
    </div>
  </template>
  
  
  <script>
  export default {
    name: "blog_index",
    
  };
  </script>
  
  <style scoped>
  .blog-index {
    font-family: Arial, sans-serif;
    color: #333;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color:#e2e8f0;
  }
  
  .header {
    background-color:#1e293b;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    color:#0f172a;
  }
  
  .nav {
    display: flex;
    justify-content: center;
    gap:20px;
  }
  
  .nav-item {
    text-decoration: none;
    color: #007bff;
    font-weight: bold;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background-color 0.3s;
  }
  
  .nav-item:hover {
    background-color: #e2e6ea;
  }
  
  .content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex:1;
    gap:20px;
    padding:10rem;
  }
  
  .footer {
    background-color: #1e293b;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
    color:#fde047;
  }
  h1{
    color:#1d4ed8;
    font-family:'Courier New', Courier, monospace;
    font-weight:bold;
  }
  p{
    font-size:20px;
    font-family:'Courier New', Courier, monospace;
  }
  .content p{
    font-size: 25px;
    font-weight:bold;
  }
  </style>
  