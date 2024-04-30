<template>
    <div >
        <v-form  @submit.prevent="createUser()">
            <div>
                <v-text-field   v-model="user.UserID" type="number" label="UserID" />
                <v-text-field v-model="user.Password" type="text" label="Password" />
                <v-select ref="select" v-model="selectedItems" :items="user.roles" label="Select" multiple chips
                    hint="What are the target regions" persistent-hint :max-items="2"
                    @change="checkMaxItems"></v-select>
                <v-text-field v-model="user.Firstname" type="text" label="Firstname" />
                <v-text-field v-model="user.Lastname" type="text" label="Lastname" />
                <v-text-field v-model="user.Callname" type="text" label="Callname" />

                <v-btn  type="submit">Create</v-btn>


            </div>
        </v-form>
    </div>
</template>

<script>
export default {
    name: 'CreatePage',
    data() {
        return {
            drawer: false,
            group: null,
            selectedItems: [],
            user: {
                UserID: 12345,
                Password: '123456',
                roles: ["user"],
                Firstname: 'test',
                Lastname: 'test',
                Callname: 'test'
            },
            roles: ['admin', 'user'] // สมมติว่ามี roles ที่เป็นไปได้
        };
    },
    mounted() {

    },
    methods: {
        checkMaxItems() {
            if (this.selectedItems.length > 2) {
                // ถ้าเลือกเกิน 2 ตัวเลือกให้แสดงข้อความแจ้งเตือน
                this.selectedItems.pop(); // ลบตัวเลือกล่าสุดที่เพิ่มเข้าไ
                alert('You can only select up to 2 items');
            }
        },
        // async testCreate() {
        //     try {
        //         const response = await fetch('http://192.168.1.160:8080/api/Jmeet/signup', {
        //             method: 'POST',
        //             headers: {
        //                 'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNCwiaWF0IjoxNzE0MDEyNTM4LCJleHAiOjE3MTQwOTg5Mzh9.I7dQq5tIMHvSt9znicNlhyPSOGCCPKwci1ibujm9VIc',
        //                 'Content-Type': 'application/json' // ต้องระบุ Content-Type เป็น application/json เมื่อส่งข้อมูล JSON
        //             },
        //             body: JSON.stringify({
        //                 "UserID": 12345,
        //                 "Password": "123456",
        //                 "roles": ["user"],
        //                 "Firstname": "test",
        //                 "Lastname": "test",
        //                 "Callname": "test"
        //             }),
        //         });

        //         // ตรวจสอบว่าการส่งคำขอสำเร็จหรือไม่
        //         if (response.ok) {
        //             const data = await response.json(); // แปลงข้อมูล JSON ที่ได้จากเซิร์ฟเวอร์เป็น Object
        //             console.log('User created:', data);
        //         } else {
        //             console.error('Failed to create user:', response.status, response.statusText);
        //         }
        //     } catch (error) {
        //         console.error('Error creating user:', error);
        //     }
        // },
        async createUser() {
            console.log(typeof this.user.roles);
            try {
                const response = await this.$axios.post('http://192.168.1.160:8080/api/Jmeet/signup', {
                    method: 'POST',
                    headers: {
                        'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNCwiaWF0IjoxNzE0MTI1MjExLCJleHAiOjE3MTQyMTE2MTF9.uz_vbWK447f9e-YpbtvkzPDdaXyg1P4j6YKuNhsBonk',
                        // 'Content-Type': 'application/json'
                    },
                    // body: {}
                    body: JSON.stringify({
                        "UserID": 123457,
                        "Password": "123456",
                        "roles": ["user"],
                        "Firstname": "test",
                        "Lastname": "test",
                        "Callname": "test"
                    }),
                });

                if (response.ok) {
                    alert('User created successfully!');
                    this.$router.push('/Home');
                } else {
                    // alert('Error creating user. Please try again later.');
                }
            } catch (error) {
                console.error('Error creating user:', error);
                // alert('Error creating user. Please try again later.');
            }
        }
        // async createUser() {
        //     try {
        //         const response = await this.$axios.post('http://192.168.1.160:8080/api/Jmeet/signup', {
        //             "UserID": this.user.UserID,
        //             "Password": this.user.Password,
        //             "roles": this.user.roles,
        //             "Firstname": this.user.Firstname,
        //             "Lastname": this.user.Lastname,
        //             "Callname": this.user.Callname
        //         });

        //         if (response.status === 200) {
        //             alert('User created successfully!');
        //             this.$router.push('/Home');
        //         } else {
        //             alert('Error creating user. Please try again later.');
        //         }
        //     } catch (error) {
        //         console.error('Error creating user:', error);
        //         alert('Error creating user. Please try again later.');
        //     }
        // }


    },
}
</script>