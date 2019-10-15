<template>
  <div>
    <v-container>
      <div>
        <v-row align="center">
          <v-col cols="4">
            <v-img src="../assets/logo.png" max-height="100px" max-width="100px" class="mx-auto"></v-img>
          </v-col>
          <v-col cols="8">
            <div id="el1">
              <v-row align="center">
                <v-col cols="6">
                  <span>닉네임</span>
                </v-col>
                <v-col cols="2">
                  <v-btn class="ma-2" color="orange darken-2" dark>
                    수정하기
                  </v-btn>
                </v-col>
              </v-row>
            </div>
            <div>
              <v-row>
                <v-col cols="3">
                  <span>참여모임 50</span>
                </v-col>
                <v-col cols="3">
                  <span>팔로워 100</span>
                </v-col>
                <v-col cols="3">
                  <span>팔로우 130</span>
                </v-col>
              </v-row>
            </div>
            <div id="el2">
              <v-chip
                v-for="i in this.tags"
                :key="i"
                class="ma-2"
                color="indigo"
                text-color="white"
              >
                <v-avatar left>
                  <v-icon>mdi-account-circle</v-icon>
                </v-avatar>
                {{i}}
              </v-chip>
            </div>
          </v-col>
        </v-row>
      </div>

      <v-divider></v-divider>

      <div>
        <h2>참여 목록 페이지</h2>
        <v-card>
          <v-tabs
            v-model="tab"
            background-color="deep-purple accent-4"
            centered
            dark
            icons-and-text
          >
            <v-tabs-slider></v-tabs-slider>

            <v-tab href="#tab-1">
              찜리스트
              <v-icon>mdi-phone</v-icon>
            </v-tab>

            <v-tab href="#tab-2">
              참여한모임
              <v-icon>mdi-heart</v-icon>
            </v-tab>

            <v-tab href="#tab-3">
              참여예정모임
              <v-icon>mdi-account-box</v-icon>
            </v-tab>
          </v-tabs>

          <v-tabs-items v-model="tab">
            <v-tab-item
              v-for="i in 3"
              :key="i"
              :value="'tab-' + i"
            >
              <v-card flat>
                <v-card-text>{{ text[i-1] }}</v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </div>

    </v-container>
  </div>
</template>

<script>
export default {
  name: 'UserPage',
  data: () => ({
      tags: [
        '스포츠',
        '독서',
        '여행'
      ],
      tab: null,
      text: [
        '찜 리스트',
        '참여했던 리스트',
        '참여예정 리스트'
      ]
    }
  ),
}
</script>

<style>
#el1 {
  height: 50%;
}
#el2 {
  height: 50%;
}
</style>