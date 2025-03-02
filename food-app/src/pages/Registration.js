import React, { useState } from 'react';
import axios from 'axios';
import './Registration.css';

const Registration = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        password2: ''
    });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleRegistration = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess('');

        if (formData.password !== formData.password2) {
            setError("Passwords do not match.");
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/register/', formData);
            setSuccess(response.data.message);
            setFormData({ username: '', email: '', password: '', password2: '' });
        } catch (err) {
            setError(err.response?.data?.detail || "Registration failed.");
        }
    };

    return (
        <div className="registration-container">
            <form className="registration-form" onSubmit={handleRegistration}>
                <h2>Register</h2>
                {error && <p className="error-message">{error}</p>}
                {success && <p className="success-message">{success}</p>}

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                />

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                />

                <input
                    type="password"
                    name="password2"
                    placeholder="Confirm Password"
                    value={formData.password2}
                    onChange={handleChange}
                    required
                />

                <button type="submit">Register</button>
                <p className="login-link">Already have an account? <a href="/login">Login</a></p>
            </form>
        </div>
    );
};

export default Registration;