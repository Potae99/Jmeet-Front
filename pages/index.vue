<template>
  <div>
      <!-- ซ่อน Navigation Drawer โดยกำหนด v-if เมื่อยังไม่ล็อกอิน -->

      <!-- App Bar -->
      <v-app-bar app :clipped-left="clipped" fixed>
          <!-- ปุ่มเมนู Navigation Drawer จะไม่แสดงเมื่อยังไม่ล็อกอิน -->
          <!-- <v-app-bar-nav-icon v-if="!loggedIn" @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
          <v-toolbar-title>{{ title }}</v-toolbar-title>
          <!-- ปุ่มอื่น ๆ ใน App Bar -->
      </v-app-bar>

      <!-- เนื้อหาของหน้า login -->
      <v-main>
          <v-container>
              <!-- ฟอร์มล็อกอิน -->
              <v-text-field label="Username" v-model="UserID"></v-text-field>
              <v-text-field label="Password" v-model="Password" type="password"></v-text-field>
              <v-btn @click="login">Login</v-btn>
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
          loggedIn: false  // เพิ่มตัวแปร loggedIn เพื่อบอกว่า user ล็อกอินหรือไม่
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
        this.$router.push('/Home');

        console.log(res);
        } catch (error) {
          console.log('eroro',error);
        }
        
        // const response = await fetch('http://192.168.1.160:8080/api/Jmeet/signin',{
        //   method: 'POST',
        //   headers: {
        //     'Content-Type': 'application/json'
        //   },
        //   body: JSON.stringify({
        //     UserID: this.UserID,
        //     Password: this.Password
        //   })
        // });
        // const data = await response.json();
        // this.users = data;
        // console.log(data);
        // this.$router.push('/Home');
      }
    //   login() {
    //       // เช็คว่า email และ password ตรงกับข้อมูลที่กำหนดหรือไม่
    //       if (this.username === 'test' && this.password === '123') {
    //         console.log(`if`);
    //           // ถ้าตรงให้ทำการล็อกอินเสร็จสิ้น
    //           this.loggedIn = true;
    //           // และนำทางไปยังหน้า inspire
    //           this.$router.push('/inspire');
    //       } else {
    //           // ถ้าไม่ตรงให้แสดงข้อความแจ้งเตือน
    //           alert('Invalid email or password!');
    //       }
    //   }
  }
};
</script>
