import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import CourseList from './components/courseList';
import CourseDetails from './components/CourseDetails';
import Register from './components/Auth/Register';
import Login from './components/Auth/login';
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
    return (
        <Router>
            <div>
                <h1>Welcome to the E-learning Platform</h1>
                <Routes>
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    <Route 
                        path="/courses" 
                        element={
                            <ProtectedRoute>
                                <CourseList />
                            </ProtectedRoute>
                        } 
                    />
                    <Route
                        path='/courses/:id'
                        element={
                            <ProtectedRoute>
                                <CourseDetails />
                            </ProtectedRoute>
                        }
                    />

                    <Route path="/" element={<Navigate to="/login" />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
