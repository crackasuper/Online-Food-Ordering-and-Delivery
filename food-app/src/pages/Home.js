import React, { useState } from 'react'; // Import useState
import './Home.css'; // Assuming there's a CSS file for styling

const Home = () => {
    const [searchQuery, setSearchQuery] = useState(''); // State for search query
    const foodItems = [
        { name: 'Food Item 1', description: 'Description of food item 1.' },
        { name: 'Food Item 2', description: 'Description of food item 2.' },
        // Add more food items as needed
    ];

    const handleSearchChange = (e) => {
        setSearchQuery(e.target.value);
    };

    const filteredFoodItems = foodItems.filter(item =>
        item.name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="home">
            <header className="home-header">
                <h1>Welcome to the Food Ordering System</h1>
                <input
                    type="text"
                    placeholder="Search for food..."
                    className="search-bar"
                    value={searchQuery}
                    onChange={handleSearchChange}
                />
            </header>
            <main className="food-list">
                <h2>Available Food Items</h2>
                {filteredFoodItems.map((item, index) => (
                    <div className="food-item" key={index}>
                        <h3>{item.name}</h3>
                        <p>{item.description}</p>
                        <button>Add to Cart</button>
                    </div>
                ))}
                {/* Add more food items as needed */}
            </main>
        </div>
    );
};

export default Home;
