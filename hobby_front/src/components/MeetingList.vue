<template>
    <div>
        <v-layout wrap>
            <v-flex v-for="i in this.Meetings.length" v-bind:key="i" xs12 sm6 md4>
                <Meeting class='ma-3'></Meeting>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import Meeting from '@/components/Meeting'

export default {
    name: 'MeetingList',
    data() {
        return {
            Meetings: [1, 2, 3, 4, 5, 6]
        }
    },
    components: {
        Meeting
    }
}
</script>

<style>

</style>