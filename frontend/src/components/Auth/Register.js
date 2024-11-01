import React, { useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

const Register = () => {
    const [username, setUsername ] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('student');
    const [message, setMessage] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage(null);
        setError(null);

        try {
            const response = await axios.post('http://localhost:8000/api/auth/register/',{
                username,
                email,
                password,
                role
            });

            setMessage(response.data.message);
            setUsername('');
            setEmail('');
            setPassword('');
            setRole('student');

        } catch (err) {
            setError(err.response.data.error || 'An error occurred');
        }

    };

    return (
        <div>
        <h1>Register</h1>
        <form onSubmit={handleSubmit}>
            <div>
                <label >Username:</label>
                <input 
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
                />
            </div>

            <div>
                <label>Email:</label>
                <input
                    type='email'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Password:</label>
                <input
                type="password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                />
            </div>

            <div>
                <label>Role:</label>
                <select value={role} onChange={(e)=> setRole(e.target.value)}>
                    <option value="student">Student</option>
                    <option value="instructor">Instructor</option>
                </select>
            </div>
            <button type="submit">Register</button>
            
        </form>
        {message && <p> {message} </p>}
        {error && <p style={{color: 'red'}}>{error}</p> }

        <p>
                Already have an account? <Link to="/login">Login here</Link>
            </p>
        </div>
    );
};

export default Register;