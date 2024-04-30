<template>
  <div  >
      <!-- ซ่อน Navigation Drawer โดยกำหนด v-if เมื่อยังไม่ล็อกอิน -->

      <!-- App Bar -->
      <v-app-bar class=" red darken-4"  app :clipped-left="clipped" fixed>
          <!-- ปุ่มเมนู Navigation Drawer จะไม่แสดงเมื่อยังไม่ล็อกอิน -->
          <!-- <v-app-bar-nav-icon v-if="!loggedIn" @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
          <v-toolbar-title class="text-h3 white--text font-weight-medium" >{{ title }}</v-toolbar-title>
          <!-- ปุ่มอื่น ๆ ใน App Bar -->
      </v-app-bar>

      <!-- เนื้อหาของหน้า login -->
      <v-main class="" >
          <v-container class="login-wrap ">
              <!-- ฟอร์มล็อกอิน -->
              <v-text-field label="Username"  v-model="UserID"></v-text-field>
              <v-text-field label="Password" v-model="Password" type="password"></v-text-field>
              <v-btn class="red darken-4 white--text" @click="login">Login</v-btn>
          </v-container>
      </v-main>
  </div>
</template>

<script>
import env from '@/env';

export default {
  data() {
      return {
          drawer: false,
          clipped: false,
          title: 'Login',
          UserID: '1234', // เปลี่ยนเป็น email แทน username
          Password: 'admin1234', // เพิ่ม password เข้ามาเก็บค่าพาสเวิร์ด
          loggedIn: false,  // เพิ่มตัวแปร loggedIn เพื่อบอกว่า user ล็อกอินหรือไม่
          Post:[]
      };
  },
  mounted() {
    
  },
  methods: {
    
      async login() {
        console.log();
        try {
        //   const res = await this.$axios.$post('http://192.168.1.160:8080/api/Jmeet/signin', {
        //   UserID: this.UserID,
        //   Password: this.Password
          
        // })
        const res = await this.$axios.$post(env.loginUrl, {
          UserID: this.UserID,
          Password: this.Password
          
        })
        return{posts:data}
        .then(this.$router.push('/Home'));

        console.log(res);
        } catch (error) {
          console.log('eroro',error);
          console.log(data.Post)
        }
        

      }

  }
};
</script>
