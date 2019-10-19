<template>
    <div>
        <v-container>
            <v-row justify="center">
                <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" dark v-on="on">결제하기</v-btn>
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
            </v-row>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Payment',
    data: () => ({
      dialog: false,
      items: [5000, 10000, 20000],
      value:''
    }),
    methods:{
        pay(){
            console.log(this.value)
            // baseUrl 부분은 서버 배포시 수정해야 하는 부분이기 때문에 store에 저장해서 가저오는게 하나로 관리하기가 편할것 같습니다.
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            form.append('amount', this.value)
            // 유저 아이디 넣어주기
            // form.append('userId', this.userName)
            axios.post(baseUrl+"accounts/kakaoPay/", form)
            .then(res =>{
                let payUrl = res.data.next_redirect_pc_url
                console.log(res)
                location.href = payUrl
                /*
                결제 끝나고 현재 home으로 이동하기 때문에 개인 유저 페이지로 돌아가게끔 router를 생성해주고
                해당 router주소를 알려주시면 백엔드에서 처리하겠습니다.
                */  
            })
            .catch(e =>{
                alert("에러가 발생했습니다. 다시 시도해주세요")
                this.$router.push('/')
            })
        }
    }
}
</script>