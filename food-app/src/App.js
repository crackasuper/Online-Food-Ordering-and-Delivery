import logo from './logo.svg';
import './App.css';
import Home from './pages/Home';
import Login from './pages/Login';
import FoodList from './pages/FoodList';


function App() {
  return (
      <Router>
          <Switch>
              <Route exact path="/" component={Home} />
              <Route path="/login" component={Login} />
              <Route path="/foods" component={FoodList} />
          </Switch>
      </Router>
  );
}

export default App;
