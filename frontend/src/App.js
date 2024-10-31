import React , { useEffect, useState } from 'react';
import CourseList from './components/courseList';
import Register from './components/Auth/Register';


const App = () => {
  return(
    <div>
      <h1>Welcome to the E-learning Platform</h1>
      <Register/>
      <CourseList/>
    </div>
  );
};

export default App;