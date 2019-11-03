<template>
  <div>
    <v-container>
      <div>
        <v-row align="center">
          <v-card id="contain_card" class="my-10">
            <v-row>
              <v-card
              class="mx-auto my-auto"
              max-width="344"
              elevation="0"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-avatar size="150">
                      <img
                        src="../assets/logo.png"
                      >
                    </v-avatar>
                    <v-list-item-title class="headline mb-1 text-center">
                      상대유저이름
                      <v-btn
                      class="ma-2"
                      color="#9AB878"
                      small
                      dark
                      >
                        팔로우
                      </v-btn>
                    </v-list-item-title>
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-chip
                        class="ma-1"
                        color="#F3B749"
                        text-color="white"
                        >
                          선호카테고리 보여주기
                        </v-chip>
                      </div>
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
              <v-divider class="my-5" vertical></v-divider>
              <v-card
              class="mx-auto my-auto"
              max-width="344"
              elevation="0"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <v-img
                    src="../assets/logo.png"
                    max-height="100px"
                    max-width="100px"
                    class="mx-auto"
                    ></v-img>(등급아이콘)
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-row>
                          <v-col cols="4" >
                            <span>참여모임 {{bandCount}}</span>
                          </v-col>
                          <v-col cols="4">
                            <v-dialog
                            v-model="followerdialog"
                            scrollable
                            max-width="300px"
                            >
                              <template v-slot:activator="{ on }">
                                <span v-on="on">팔로워 {{followerCounting}}</span>
                              </template>
                              <!-- 팔로워 목록 모달 -->
                              <v-card>
                                <v-card-title>팔로워</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="height: 300px;">
                                  <v-list v-if="followerCounting">
                                    <v-list-item 
                                    v-for="item in followerGroup"
                                    :key="item.name"
                                    >
                                      <v-list-item-avatar>
                                        <v-img :src="item.img"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title v-text="item.name">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
                                  </v-list>
                                  <v-list v-else>
                                    <v-list-item-content>
                                        <h3>팔로워가 없습니다 !</h3>
                                      </v-list-item-content>
                                  </v-list>
                                </v-card-text>
                                <v-divider></v-divider>
                                <v-card-actions>
                                  <v-btn
                                  color="#2E1E11"
                                  text
                                  @click="followerdialog = false"
                                  >
                                    Close
                                  </v-btn>
                                </v-card-actions>
                              </v-card>
                            </v-dialog>
                          </v-col>
                          <v-col cols="4">
                            <v-dialog
                            v-model="followdialog"
                            scrollable
                            max-width="300px"
                            >
                              <template v-slot:activator="{ on }">
                                <span v-on="on">팔로잉 {{followCounting}}</span>
                              </template>
                              <!-- 팔로우 목록 모달 -->
                              <v-card>
                                <v-card-title>팔로잉</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="height: 300px;">
                                  <v-list v-if="followCounting">
                                    <v-list-item
                                    v-for="item in followGroup"
                                    :key="item.title"
                                    >
                                      <v-list-item-avatar>
                                        <v-img :src="item.img"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title v-text="item.name">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
                                  </v-list>
                                  <v-list v-else>
                                    <h3>팔로잉한 사람이 없습니다 !</h3>
                                  </v-list>
                                </v-card-text>
                                <v-divider></v-divider>
                                <v-card-actions>
                                  <v-btn
                                  color="#2E1E11"
                                  text
                                  @click="followdialog = false"
                                  >
                                    Close
                                  </v-btn>
                                </v-card-actions>
                              </v-card>
                            </v-dialog>
                          </v-col>
                        </v-row>
                      </div>
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-row>
          </v-card>
        </v-row>
      </div>
      <!-- 유저가 참여한 목록 -->
      <div>
        <v-timeline align-top :dense="$vuetify.breakpoint.smAndDown">
            <v-timeline-item
            v-for="(item, i) in items"
            :key="i"
            color="#EE7785"
            >
            <template v-slot:opposite>
                <span
                :class="`headline font-weight-bold ${item.color}--text`"
                v-text="item.day"
                ></span>
            </template>
            <v-card class="elevation-2">
                <v-card-title class="headline">제목</v-card-title>
                <v-card-text>
                    <p>상세내용</p>
                </v-card-text>
            </v-card>
            </v-timeline-item>
        </v-timeline>
      </div>
    </v-container>
  </div>
</template>

<script>
import Payment from '@/components/Payment'

export default {
  name: 'UserPage',
  components: {
    Payment
  },
  data () {
    return {
      items: [
        {
          day: '2019.01.01',
          color: 'indigo',
          icon: 'mdi-star',
        },
        {
          day: '2019.01.01',
          color: 'indigo',
          icon: 'mdi-book-variant',
        },
        {
          day: '2019.01.01',
          color: 'success',
          icon: 'mdi-airballoon',
        },
        {
          day: '2019.01.01',
          color: 'indigo',
          icon: 'mdi-buffer',
        },
      ],
    }
  }
}
</script>

<style lang="stylus">
#contain_card
  width 100%
</style>
