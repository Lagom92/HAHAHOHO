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
                    <v-img
                    src="../assets/logo.png"
                    max-height="100px"
                    max-width="100px"
                    class="mx-auto"
                    ></v-img>
                    <v-list-item-title class="headline mb-1 text-center">
                      닉네임
                      <v-btn
                      class="ma-2"
                      color="#9AB878"
                      fab
                      outlined
                      x-small
                      dark
                      >
                        <v-icon>mdi-account-edit</v-icon>
                      </v-btn>
                    </v-list-item-title>
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-chip
                        v-for="i in this.tags"
                        :key="i"
                        class="ma-1"
                        color="#F3B749"
                        text-color="white"
                        >
                          {{i}}
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
                    ></v-img>(등급아이콘자리)
                    <v-list-item-title class="headline mb-1 text-center">
                      <v-row justify="center">
                        <span class="my-auto mr-3">포인트 5,000 P</span>
                        <Payment></Payment>
                      </v-row>
                    </v-list-item-title>
                    <v-list-item-subtitle class="text-center">
                      <div>
                        <v-row>
                          <v-col cols="4" >
                            <span>참여모임 50</span>
                          </v-col>
                          <v-col cols="4">
                            <v-dialog
                            v-model="followerdialog"
                            scrollable
                            max-width="300px"
                            >
                              <template v-slot:activator="{ on }">
                                <span v-on="on">팔로워 100</span>
                              </template>
                              <!-- 팔로워 목록 모달 -->
                              <v-card>
                                <v-card-title>팔로워</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="height: 300px;">
                                  <v-list>
                                    <v-list-item
                                    v-for="item in items"
                                    :key="item.title"
                                    >
                                      <v-list-item-avatar>
                                        <v-img :src="item.avatar"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title v-text="item.title">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
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
                                <span v-on="on">팔로우 5</span>
                              </template>
                              <!-- 팔로우 목록 모달 -->
                              <v-card>
                                <v-card-title>팔로우</v-card-title>
                                <v-divider></v-divider>
                                <v-card-text style="height: 300px;">
                                  <v-list>
                                    <v-list-item
                                    v-for="item in items"
                                    :key="item.title"
                                    >
                                      <v-list-item-avatar>
                                        <v-img :src="item.avatar"></v-img>
                                      </v-list-item-avatar>
                                      <v-list-item-content>
                                        <v-list-item-title v-text="item.title">
                                        </v-list-item-title>
                                      </v-list-item-content>
                                    </v-list-item>
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
      <div>
        <v-card>
          <v-tabs vertical color="#F3B749">
            <v-tab>
              <v-icon left>mdi-account</v-icon>
              찜목록
            </v-tab>
            <v-tab>
              <v-icon left>mdi-lock</v-icon>
              참여예정 목록
            </v-tab>
            <v-tab>
              <v-icon left>mdi-access-point</v-icon>
              참여한 목록
            </v-tab>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <p class="mb-0">찜목록</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <p class="mb-0">참여예정 목록</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <p class="mb-0">참여한 목록</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-card>
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
      tags: [
        '스포츠',
        '독서',
        '여행'
      ],
      followdialog: false,
      followerdialog: false,
      items: [
        {
          title: 'Jason Oner',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg'
        },
        {
          title: 'Travis Howard',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg'
        },
        {
          title: 'Ali Connors',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg'
        },
        {
          title: 'Cindy Baker',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg'
        }
      ]
    }
  }
}
</script>

<style lang="stylus">
#contain_card
  width 100%
</style>
