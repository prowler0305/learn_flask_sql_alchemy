<template>
  <table class="table table-hover">
    <thead class="thead-dark">
    <tr>
      <th scope="col"></th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Street</th>
      <th scope="col">City</th>
      <th scope="col">State</th>
      <th scope="col">Zip</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="student in students" :key="student.id">
      <td>
        <button type="button" class="btn btn-outline-primary" data-toggle="modal" data-target="#editStudentModal" :data-student-id="student.id">
          Edit
        </button>
      </td>
      <td>{{ student.first_name }}</td>
      <td>{{ student.last_name }}</td>
      <td>{{ student.street }}</td>
      <td>{{ student.city }}</td>
      <td>{{ student.state }}</td>
      <td>{{ student.zip }}</td>
    </tr>
    </tbody>
  </table>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  const students = ref([]);
  const fetch_students = async function() {
    try {
      const response = await axios.get('http://localhost:5000/api/students');
      if (response.status === 200) {
        students.value = response.data;
        console.log(students.value);
        console.log(response.data);
      } else {
        const errorMessage = response.data.error || "Unknown error fetching students";
        console.error(errorMessage);
        alert(errorMessage);
      }
    } catch (error) {
      console.error('Error attempting fetching of students:', error.message);
      alert(error.message);
    }
  }
  onMounted(() => {
    fetch_students();
  });
</script>