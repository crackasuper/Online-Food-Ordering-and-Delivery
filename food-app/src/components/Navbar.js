import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="nav-links">
                <Link to="/">Home</Link>
                <Link to="/login">Login</Link>
                <Link to="/registration">Register</Link>
            </div>
            <div className="cart-icon">🛒</div>
        </nav>
    );
};

export default Navbar;