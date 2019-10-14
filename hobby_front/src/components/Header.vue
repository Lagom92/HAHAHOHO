<template>
  <div>
    <v-toolbar fixed>
      <v-container>
        <v-row>
          <v-col md="2">
            <v-toolbar-title>하하호호</v-toolbar-title>
          </v-col>

          <v-col md="3">
            <v-btn text>모임</v-btn>
            <v-btn text>커뮤니티</v-btn>
          </v-col>
          
          <v-col md="2" offset-md="5">
            <v-btn text>로그인</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-toolbar>
  </div>
</template>

<script>
export default {
    name: 'Header',
}
</script>