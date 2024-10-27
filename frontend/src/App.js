import React , { useEffect, useState } from 'react';
import axios from 'axios';
import CourseList from './components/courseList';


const App = () => {
  return(
    <div>
      <CourseList />
    </div>
  );
};

export default App;