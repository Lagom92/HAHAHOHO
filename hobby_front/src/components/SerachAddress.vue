<template>
  <div>
    <form id="form" name="form" method="post">
      <table >
        <colgroup>
          <col style="width:20%"><col>
        </colgroup>
        <tbody>
          <tr>
            <th>우편번호</th>
            <td>
              <input type="hidden" id="confmKey" name="confmKey" value="">
              <input type="text" id="zipNo" name="zipNo" readonly>
              <input type="button" value="주소검색" @click="goPopup()">
            </td>
          </tr>
          <tr>
            <th>도로명주소</th>
            <td><input type="text" id="roadAddrPart1"></td>
          </tr>
          <tr>
            <th>상세주소</th>
            <td>
              <input type="text" id="addrDetail" value="">
              <input type="text" id="roadAddrPart2" value="">
            </td>
          </tr>
        </tbody>
      </table>
    </form>
  </div>
</template>

<script>

export default {
  name: 'SerachAddress',
  data () {
    return {
      dialog: false
    }
  },
  methods: {
    goPopup () {
      window.open(
        'http://www.juso.go.kr/addrlink/addrLinkUrl.do',
        'pop',
        'width=570,height=420, scrollbars=yes, resizable=yes'
      )
    }
  }
}
</script>

<style lang="stylus">
#zipNo
  width 100px

#roadAddrPart1
  width 85%

#addrDetail
  width 40%

#roadAddrPart2
  width 40%
</style>
