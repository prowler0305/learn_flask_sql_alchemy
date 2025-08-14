import 'bootstrap'
import {createApp} from "vue";
// import router from "./router";

import NavBar from "./components/NavBar.vue"
import student_table_data from "./components/student_table_data.vue";
const nav_bar_component = createApp(NavBar);
nav_bar_component.mount("#navbar");
const student_table_data_component = createApp(student_table_data);
student_table_data_component.mount("#student-table-data");
