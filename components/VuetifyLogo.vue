<template>
  <img class="vuetify-logo" alt="Vuetify Logo" src="/vuetify-logo.svg">
</template>

<style>
.vuetify-logo {
  height: 180px;
  width: 180px;
  transform: rotateY(560deg);
  animation: turn 3.5s ease-out forwards 1s;
}

.bordered-item {
  border-bottom: 1px solid #ccc;
  /* Example border style */
}

.bordered-login {
  border-width: 3px;
  border-style: solid;
  padding: 25px;
  border-radius: 25px;
  width:50%;

}
.login-wrap {
    position: relative;
    margin: 0 auto;
    background: #ccc;
    width: 350px;
    border-radius: 5px;
    box-shadow: 3px 3px 10px #333;
    padding: 15px;

    }


@keyframes turn {
  100% {
    transform: rotateY(0deg);
  }
}
</style>
