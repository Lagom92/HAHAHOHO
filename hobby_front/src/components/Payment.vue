<template>
  <div>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn class="ma-2" color="#9AB878" fab outlined x-small dark v-on="on">
          <v-icon>mdi-credit-card-outline</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">결제 정보 입력</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-select
                :items="items"
                v-model="value"
                label="충전금액*"
                required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>결제는 카카오페이로 진행됩니다</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">취소</v-btn>
          <v-btn color="blue darken-1" text @click="pay">결제</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Payment',
  data () {
    return {
      dialog: false,
      items: [5000, 10000, 20000],
      value: ''
    }
  },
  methods: {
    pay () {
      let form = new FormData()
      form.append('amount', this.value)
      form.append('userId', this.$store.state.user_id)
      axios.post(this.$store.state.baseUrl + 'accounts/kakaoPay', form)
        .then(res => {
          let payUrl = res.data.next_redirect_pc_url
          location.href = payUrl
        })
        .catch(e => {
          alert('에러가 발생했습니다. 다시 시도해주세요')
          this.$router.push('/')
        })
    }
  }
}
</script>
