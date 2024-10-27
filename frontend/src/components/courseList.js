import React, {useEffect, useState} from 'react';
import { getCourses } from '../services/courseService';


const CourseList = () => {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const data = await getCourses();
                setCourses(data);
            } catch (err){
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchCourses();
    }, []);

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error fetching courses:{error.message}</div>;

    return (
        <div>
            <h1>Course List</h1>
            <ul>
                {courses.map(course =>(
                    <li key={course.id}>
                    <h2>{course.title}</h2>
                    <p>{course.description}</p>
                    <p>Price: ${course.price}</p>
                </li>
                ))}
            </ul>
        </div>
    );
};

export default CourseList