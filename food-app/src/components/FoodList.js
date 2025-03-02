
// src/components/FoodList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FoodList() {
    const [foods, setFoods] = useState([]);
    const token = localStorage.getItem('token');  // Retrieve the token
    useEffect(() => {
        axios.get('/api/foods/',  { headers: { Authorization: `Token ${token}` } }) // add authorization headers
            .then(response => {
                setFoods(response.data);
            })
            .catch(error => {
                console.error('Error fetching foods:', error);
            });
    }, []);

    return (
        <ul>
            {foods.map(food => (
                <li key={food.id}>{food.food_name} - ${food.food_price}</li>
            ))}
        </ul>
    );
}

export default FoodList;