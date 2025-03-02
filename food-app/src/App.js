
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar'; // Importing the Navbar component


import './App.css';
import Home from './pages/Home';
import Login from './pages/Login';
import FoodList from './components/FoodList';
import Registration from './pages/Registration';

function App() {
  return (
    <Router>
      <Navbar /> {/* Adding the Navbar component */}
      <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/registration" element={<Registration />} />
        <Route path="/foods" element={<FoodList />} />
      </Routes>
    </Router>
  );
}

export default App;
