<template>
    <div>
        <TopBanner></TopBanner>
        <v-container>
            <div>
                <h1>모임 목록</h1>
            </div>
            <v-layout>
                <v-flex>
                    <MeetingList></MeetingList>    
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import TopBanner from '../components/TopBanner'
import MeetingList from '../components/MeetingList'

export default {
    name: 'ListPage',
    components: {
        MeetingList,
        TopBanner
    }
}
</script>

<style>

</style>