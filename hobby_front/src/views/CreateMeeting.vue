<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="12" md="6" offset-md="3">
                    <div>
                        <h1>모임 생성</h1>
                    </div>
                    <v-divider></v-divider>

                    <v-file-input accept="image/*" label="모임 커버 사진"></v-file-input>

                     <v-form ref="form" v-model="valid">
                        <v-text-field
                            v-model="title"
                            :counter="10"
                            label="글 제목"
                        ></v-text-field>

                        <v-textarea
                            outlined
                            v-model="content"
                            label="글 내용"
                        ></v-textarea>

                          <v-row>
                            <v-col class="px-4">
                            <v-range-slider
                                v-model="agerange"
                                label="연령범위"
                                :max="agemax"
                                :min="agemin"
                                hide-details
                                thumb-label="always"
                                class="align-center"
                                track-color="grey"
                            >
                            </v-range-slider>
                        </v-col>
                    </v-row>

                        <v-row>
                            <v-col cols="12" md="6">
                                <v-select
                                    v-model="select"
                                    :items="items"
                                    label="성별"
                                    required
                                ></v-select>
                            </v-col>
                            <v-col cols="12" md="6">
                                <v-text-field
                                    v-model="num"
                                    label="최소 인원"
                                ></v-text-field>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col cols="12" md="6">
                                <v-text-field
                                    v-model="date"
                                    label="만나는 날짜"
                                ></v-text-field>
                            </v-col>
                            <v-col cols="12" md="6">
                                <v-menu
                                    ref="menu"
                                    v-model="menu2"
                                    :close-on-content-click="false"
                                    :nudge-right="40"
                                    :return-value.sync="time"
                                    transition="scale-transition"
                                    offset-y
                                    max-width="290px"
                                    min-width="290px"
                                >
                                    <template v-slot:activator="{ on }">
                                    <v-text-field
                                        v-model="time"
                                        label="만나는 시간"
                                        readonly
                                        v-on="on"
                                    ></v-text-field>
                                    </template>
                                    <v-time-picker
                                    v-if="menu2"
                                    v-model="time"
                                    full-width
                                    @click:minute="$refs.menu.save(time)"
                                    ></v-time-picker>
                                </v-menu>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="2">
                                <span>카테고리</span>
                            </v-col>
                            <v-col cols="10">
                                <v-chip-group
                                    v-model="selection"
                                    active-class="deep-purple--text text--accent-4"
                                    mandatory
                                >
                                    <v-chip>스포츠</v-chip>
                                    <v-chip>공연</v-chip>
                                    <v-chip>음악</v-chip>
                                </v-chip-group>
                            </v-col>
                        </v-row>
                        
                        <v-btn>
                            임시저장
                        </v-btn>

                        <v-btn>
                            확인
                        </v-btn>
                     </v-form>
                </v-col>

            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'createmeeting',
    data: () => ({
        valid: true,
        title: '',
        content: '',
        date: '',
        num:'',
        select: null,
        items: [
            '상관없음',
            '남성',
            '여성'
        ],
        selection: 0,
        time: null,
        menu2: false,
        agemin: 15,
        agemax: 100,
        agerange:[20,100]
    }),
}
</script>