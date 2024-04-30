<template>
  <div>
    <v-btn @click="createUser">+</v-btn>
    <v-btn @click="fullcalendar">+</v-btn>

    <div v-for="user in users" :key="user.id">
      <v-card class="mx-auto" max-width="500" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              {{ user.UserID }}
            </div>
            <v-list-item-title class="text-h5 mb-1">
              {{ user.Firstname }} {{ user.Lastname }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ user.username }}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-avatar tile size="80">
            <v-img :src="user.avatar" />
          </v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn rounded class="red" text @click="deleteUser(user.id)">
            Delete {{ user.id }}
          </v-btn>

          <v-btn rounded class="green" text @click="editUser(user.id)">
            Edit
          </v-btn>
        </v-card-actions>

        <!-- เพิ่มปุ่ม Edit และเชื่อมโยงไปยังหน้าแก้ไขข้อมูลผู้ใช้งาน -->

      </v-card>

    </div>
    <v-spacer></v-spacer>
  </div>

</template>

<script>


export default {
  name: 'HomePage',
  data() {
    return {
      drawer: false,
      group: null,
      users: [],
    };
  },
  mounted() {
    this.fetchUsers();

    // this.dataUser();
  },
  methods: {
    async fetchUsers() {
      // const response = await this.$axios.get('/api/admin/get/alluser');
      const response = await fetch('http://192.168.1.160:8080/api/admin/get/alluser',{
        method: 'GET',
        headers: {
          'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNCwiaWF0IjoxNzE0MTI1MjExLCJleHAiOjE3MTQyMTE2MTF9.uz_vbWK447f9e-YpbtvkzPDdaXyg1P4j6YKuNhsBonk'
        }
      });
      const data = await response.json();
      this.users = data;
      console.log(data);
      console.log("typeof  "+typeof this.users[0].UserID, typeof this.users[0].Password, typeof this.users[0].roles, typeof this.users[0].Firstname, typeof this.users[0].Lastname, typeof this.users[0].Callname);
    },
    async createUser() {
      this.$router.push("/create");
    },
    async editUser(id) {
      this.$router.push("/update/" + id);
    },

    async fullcalendar() {
      this.$router.push("/fullcalendar");
    },

    async deleteUser(id) {
      try {
        const response = await fetch("https://www.melivecode.com/api/users/delete", {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            id: id
          })
        });
        if (response.ok) {
          // ลบข้อมูลจากอาเรย์ users หลังจากลบข้อมูลบนเซิร์ฟเวอร์เรียบร้อย
          this.users = this.users.filter((user) => user.id !== id);
          alert('User deleted successfully!');
        } else {
          alert('Error deleting user. Please try again later.');
        }
      } catch (error) {
        console.error('Error deleting user:', error);
        alert('Error deleting user. Please try again later.');
      }
    }

  },
}
</script>
