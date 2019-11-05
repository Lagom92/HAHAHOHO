<template>
    <div>
        <full-page ref="fullpage" :options="options" id="fullpage">
            <Intro style="height:100%" class="section"/>
            <!-- 에티켓 -->
            <Etiquette class="section"/>
            <!-- 운영방침 -->
            <Rule class="section"/>
        </full-page>
    </div>
</template>

<script>
import Intro from '../components/Intro.vue'
import Etiquette from '../components/Etiquette.vue'
import Rule from '../components/Rule.vue'

export default {
    name: 'About',
    components:{
        Intro,
        Etiquette,
        Rule
    },
    data() {
        return {
            options: {
                navigation: true,
                slidesNavigation: true,
                licenseKey: 'YOUR_KEY_HERE'
            },
        }
    }
}
</script>

<style lang="stylus">

</style>