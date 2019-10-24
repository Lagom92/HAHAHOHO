<template>
    <div class="topBanner">
        <v-container id="SearchBar">
            <SearchBar></SearchBar>
        </v-container>
    </div>
</template>

<script>
import SearchBar from "./SearchBar"

export default {
    name: 'TopBanner',
    components: {
        SearchBar
    }
}
</script>

<style>
    .topBanner {
        position: relative;
        height: 50vh;
        background-color: #f2f2f2;
        margin-bottom: 50px;
    }
    #SearchBar {
        position: relative;
        width: 50vw;
        top: 70%;
    }
</style>