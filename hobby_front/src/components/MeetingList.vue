<template>
    <div>
        <v-layout>
            <v-flex v-for="i in 3" v-bind:key="i" xs12 sm6 md4>
                <Meeting class='ma-3'></Meeting>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import Meeting from '@/components/Meeting'

export default {
    name: 'MeetingList',
    components: {
        Meeting
    }
}
</script>

<style>

</style>