<template>
    <div>
        <v-container>
            <v-layout>
                <v-flex>
                    <MeetingList></MeetingList>    
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import MeetingList from '../components/MeetingList'

export default {
    name: 'ListPage',
    components: {
        MeetingList
    }
}
</script>

<style>

</style>