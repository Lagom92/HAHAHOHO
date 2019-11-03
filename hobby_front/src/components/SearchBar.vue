<template>
<div class="text-center">
  <div class="search-box">
      <input v-model="word" type="text" @keyup.enter="search()" placeholder=" " /><span></span>
  </div>
</div>
</template>

<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      word: ''
    }
  },
  methods: {
    search: function () {
      this.$store.commit('wordSave', this.word)
      var nowPosition = this.$router.history.current.name
      var searchBox = document.querySelectorAll('.search-box input[type="text"] + span');

        searchBox.forEach((elm) => {
            elm.addEventListener('click', () => {
                elm.previousElementSibling.value = '';
            });
        });
      if (nowPosition == 'search') {
        window.location.reload()
      } else {
        this.$router.replace('search')
      }
    },
  }
}
</script>

<style>
.search-box{
  display: inline-block;
  position: relative;
  border-radius: 50px;
  border: 5px solid #f1bbba;
}
.search-box span {
  width: 25px;
  height: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: -13px;
  right: -15px;
  transition: bottom 300ms ease-out 300ms, right 300ms ease-out 300ms;
}
.search-box span:before, .search-box span:after {
  content: '';
  height: 25px;
  border-left: solid 5px #f1bbba;
  position: absolute;
  transform: rotate(-45deg);
}
.search-box span:after {
  transform: rotate(45deg);
  opacity: 0;
  top: -20px;
  right: -10px;
  transition: top 300ms ease-out, right 300ms ease-out, opacity 300ms ease-out;
}
input {
  font-size: 20px;
  font-weight: bold;
  width: 54px;
  height: 54px;
  padding: 5px 40px 5px 10px;
  border: none;
  box-sizing: border-box;
  border-radius: 50px;
  background: #1a1a1a;
  transition: width 800ms cubic-bezier(0.5, -0.5, 0.5, 0.5) 600ms;
  color: #f1bbba;
}
.search-box input:focus {
  outline: none;
}
.search-box input:focus, .search-box input:not(:placeholder-shown) {
  width: 300px;
  transition: width 800ms cubic-bezier(0.5, -0.5, 0.5, 1.5);
}
.search-box input:focus + span, .search-box input:not(:placeholder-shown) + span {
  bottom: 13px;
  right: 10px;
  transition: bottom 300ms ease-out 800ms, right 300ms ease-out 800ms;
}
.search-box input:focus + span:after, .search-box input:not(:placeholder-shown) + span:after {
  top: 0;
  right: 10px;
  opacity: 1;
  transition: top 300ms ease-out 1100ms, right 300ms ease-out 1100ms, opacity 300ms ease 1100ms;
}
</style>