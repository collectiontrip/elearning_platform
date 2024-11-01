import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getCourseDetails } from '../services/courseService';

const CourseDetails = () => {
    const { id } = useParams(); // Get the course ID from the URL
    const [course, setCourse] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCourseDetails = async () => {
            try {
                const data = await getCourseDetails(id);
                setCourse(data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchCourseDetails();
    }, [id]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error fetching course details: {error.message}</div>;
    if (!course) return <div>No course found</div>;

    return (
        <div>
            <h1>{course.title}</h1>
            <p>{course.description}</p>
            <p>Price: ${course.price}</p>
        </div>
    );
};

export default CourseDetails;
