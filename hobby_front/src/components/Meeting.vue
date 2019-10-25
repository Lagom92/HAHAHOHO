<template>
    <v-card>
        <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" height="200px"/>
        <v-card-title primary-title>
            <div>
                <div class='headline'>title</div>
                <span class='grey--text'>body</span>
                <v-divider class="my-3"></v-divider>
                <v-btn text to="/list/detail">상세보기</v-btn>
            </div>
        </v-card-title>
    </v-card>
</template>

<script>
export default {
    name: 'Meeting'
}
</script>

<style>

</style>