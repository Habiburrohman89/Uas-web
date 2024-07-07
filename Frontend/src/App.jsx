import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/navabar/Navbar'; 
import Content from './components/content/content'; 
import TaskDetail from './components/content/TaskDetail'; 
import FormTugas from './components/content/TaskForm'; 
import './App.css';

function App() {

  const handleSubmit = (data) => {
    fetch('http://localhost:8000/api/tugas/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      // Lakukan sesuatu setelah sukses, misalnya tampilkan pesan atau refresh data
    })
    .catch((error) => {
      console.error('Error:', error);
      // Handle error
    });
  };

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Content />} />
        <Route path="/task/:id" element={<TaskDetail />} />
        <Route path="/new-task" element={<FormTugas onSubmit={handleSubmit} />} />
      </Routes>
    </Router>
  );
}

export default App;
