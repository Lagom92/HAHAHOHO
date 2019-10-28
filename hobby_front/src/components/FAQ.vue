<template>
  <div>
    <h1 class="mb-3">FAQ</h1>
    <v-divider id='topdivider'></v-divider>
    <v-expansion-panels focusable>
      <v-expansion-panel
        v-for="(faq,a) in items"
        :key="a"
      >
        <v-expansion-panel-header>{{faq.question}}</v-expansion-panel-header>
        <v-expansion-panel-content class="pt-5">{{faq.answer}}</v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  name: 'FAQ',
  data () {
    return {
      items: [
        {
          question: '회원가입은 어떻게 하나요?',
          answer: '저희 사이트의 회원가입은 카카오와 네이버로 로그인할 수 있습니다. 우측 상단에 있는 로그인 버튼을 눌러보세요^^',
        },
        {
          question: '포인트는 무엇인가요?',
          answer: '모임에 참여할 때 필요합니다. 신청하고 오지 않는 경우를 대비해서 만들어 놓은 것입니다. 모임에 참여하시면 포인트를 얻을 수 있으며, 카카오페이로 결제도 가능합니다^^',
        },
        {
          question: '등급이 어떻게 되는건가요?',
          answer: '등급은 브론즈 - 실버 - 골드로 구성되어있습니다. 활발한 활동을 하면 어느새 골드회원이 되어있을거에요^^',
        },
        {
          question: '회원 탈퇴는 어떻게 하나요?',
          answer: '동식@이메일.com 으로 연락주시면 회원탈퇴 처리 해드리겠습니다. 감사합니다.',
        },
      ],
    }
  }
}
</script>

<style lang="stylus">
#topdivider
  border-top-width 2px
  border-top-color #000
</style>
