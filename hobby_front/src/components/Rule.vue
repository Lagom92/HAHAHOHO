<template>
  <v-carousel id="ruleCaro" hide-delimiters>
    <v-carousel-item v-for="(slide, i) in slides" :key="i">
    <v-parallax v-if="slide==1" src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" height="900" class="pa-10 slide">
        <v-row align="center" justify="center">
            <v-col class="text-center" cols="12">
                <h1 class="display-2 font-weight-bold mb-4">하하호호 운영방침</h1>
                <h4 class="headline">하하호호 운영 방식에 대해서 알려드릴게요~</h4>
            </v-col>
        </v-row>
    </v-parallax>
    <!-- 운영방침 (회원관리) -->
    <v-parallax v-else-if="slide==2" src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" class="pa-10 slide">
        <h1>회원관리</h1>
        <v-row align="center" justify="center">
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-1-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">회원가입</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        카카오, 네이버 계정으로 로그인 할 수 있어요.
                        <br>로그인 후 더 하하호호를 즐겨보세요~
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-2-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">회원등급</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        등급은 '브론즈-실버-골드-VIP' 단계로 구성되어 있어요.
                        <br>하하호호에서 열심히 즐기다보면 어느새 VIP가 되어있겠죠?
                        <br>브론즈 : 처음 로그인 한 회원
                        <br>실버 : 정보수정을 한 회원
                        <br>골드 : 정보수정 한 후 모임에 5번 이상 참여한 회원
                        <br>VIP : 모임에 10번 이상 참여한 회원
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-3-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">회원탈퇴</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        동식@gmail.com으로 메일 보내주세요~
                        <br>더 나은 서비스를 제공할 수 있도록 언제나 노력하는 하하호호가 되겠습니다!
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-parallax>
    <!-- 운영방침 (모임) -->
    <v-parallax v-else-if="slide==3" src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" class="slide pa-10">
        <h1>모임</h1>
        <v-row align="center" justify="center">
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-1-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">모임생성</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        하고 싶은 모임이 없나요?
                        <br>'+'버튼을 눌러 직접 모임을 생성해보세요!
                        <br>모임장이 되면 1,000포인트를 얻을 수 있는 기회도 있답니다~
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-2-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">참여신청</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        하고 싶은 모임이 있다면 주저없이 '신청하기' 버튼을 눌러주세요!
                        <br>약속 시간은 꼭 지키는 매너만 있으면 OK!
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-3-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">찜하기</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        참여신청을 할지말지 고민되는 모임이 있나요?
                        <br>하트 버튼을 눌러 '찜'해보세요~
                        <br>마이페이지 달력에서도 볼 수 있습니다
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-parallax>
    <!-- 운영방침 (포인트제도) -->
    <v-parallax v-else-if="slide==4" src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" class="section pa-10">
        <h1>포인트제도</h1>
        <v-row align="center" justify="center">
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-1-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">포인트결제</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        포인트는 모임에 참여하기 위해서는 꼭 필요합니다.
                        <br>포인트가 부족할 때는 
                        <br>마이페이지에서 포인트 결제하기 버튼을 눌러주세요!
                        <br>카카오페이로 일정 금액 충전할 수 있답니다~
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-2-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">포인트사용</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        모임에 참여하기 위해서는 2,000포인트가 차감됩니다!
                        <br>노쇼를 방지하기 위해 만들어진 제도에요.
                        <br>모임에 참여하면 1,000포인트를,
                        <br>참여 후 평가를 남겨주시면 1,000포인트를 얻을 수 있으니 걱정마세요^^
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card dark color="#00ff0000" elevation="0">
                    <v-icon x-large>mdi-numeric-3-circle</v-icon>
                    <v-card-title class="headline font-weight-bold">포인트획득</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text class="title">
                        자유게시판에 글쓰면 10포인트,
                        <br>댓글 작성 시 2포인트를 얻을 수 있어요!
                        <br>하루에 최대 30포인트까지 적립 가능하답니다~
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-parallax>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
    data() {
        return {
            slides:[1,2,3,4],
        }
    }
}
</script>

<style>
#ruleCaro > div > div > div {
    height: 100% !important
}
#ruleCaro > div > div > div > div > div {
    height: 100% !important
}
</style>
