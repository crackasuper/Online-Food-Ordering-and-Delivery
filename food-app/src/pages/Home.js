import React from 'react';
import './Home.css'; // Assuming there's a CSS file for styling

const Home = () => {
    return (
        <div className="home">
            <header className="home-header">
                <h1>Welcome to the Food Ordering System</h1>
                <input type="text" placeholder="Search for food..." className="search-bar" />
            </header>
            <main className="food-list">
                <h2>Available Food Items</h2>
                {/* Placeholder for food items */}
                <div className="food-item">
                    <h3>Food Item 1</h3>
                    <p>Description of food item 1.</p>
                    <button>Add to Cart</button>
                </div>
                <div className="food-item">
                    <h3>Food Item 2</h3>
                    <p>Description of food item 2.</p>
                    <button>Add to Cart</button>
                </div>
                {/* Add more food items as needed */}
            </main>
        </div>
    );
};

export default Home;
