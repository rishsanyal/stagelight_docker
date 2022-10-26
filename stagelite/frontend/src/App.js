import logo from './logo.svg';
import './App.css';

import {
  BrowserRouter as Router,
  Route,
} from "react-router-dom";

import Topics from './pages/components/Topics';


function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path="/" name="Topics page" render={() => <Topics />} />
      </Router>
    </div>
  );
}

export default App;
