import axios from "axios";

const API_URL =  'http://localhost:8000/api/courses/';


export const getCourses = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error){
        console.error("Error fetching courses:", error);
        throw error;
    }
};

export const getCourseDetails = async (id) => {
    try {
        const response = await axios.get(`${API_URL}${id}/`);

return response.data;
    } catch (error) {
        console.error("Error fetching course details", error);
        throw error;

    }
    
};

const CourseService = {
    getCourses,
    getCourseDetails
};

export default  CourseService;