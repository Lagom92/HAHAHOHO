<template>
    <v-hover
        v-slot:default="{ hover }"
    >
        <v-card
            :elevation="hover ? 12 : 2"
        >
            <v-container class="pa-1">
                <v-item-group
                    v-model="selected"
                    multiple
                >
                    <v-item v-slot:default="{ active, toggle }">
                        <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" height="250px"
                            class="text-right pa-2"
                            @click="toggle"
                        >
                            <v-btn icon dark color="#F3B749">
                                <v-icon>
                                    {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                                </v-icon>
                            </v-btn>
                        </v-img>
                    </v-item>
                    <v-card-text class="pt-6" style="position: relative;" >
                        <v-btn
                            absolute
                            color="#F3B749"
                            class="white--text"
                            fab
                            small
                            right
                            top
                            to="/list/detail"
                        >
                            <v-icon >mdi-plus</v-icon>
                        </v-btn>
                        <div class="mb-2" >
                            <v-chip small color="#9AB878" dark>국내여행</v-chip>
                        </div>
                        <h3 class="headline mb-2" color="#F3B749">제목입니다제목</h3>
                        <v-divider class="my-3"></v-divider>
                        <v-row class="pl-3">
                            <v-col class="pa-0">
                                <v-icon small>mdi-clock-outline</v-icon> 2019-10-31 오후 6시
                            </v-col>
                            <v-col class="pa-0">
                                <v-icon small>mdi-map-marker</v-icon> 광주 서구
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-item-group>
            </v-container>
        </v-card>
    </v-hover>
</template>

<script>
export default {
    name: 'Meeting',
    data() {
        return {
        selected: [],
        }
    }
}
</script>

<style>

</style>