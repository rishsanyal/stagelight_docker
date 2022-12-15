import logo from './logo.svg';
import './App.css';

import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Topics from './pages/components/Topics';
import TopicSubmission from './pages/components/TopicSubmission';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/topics" name="Topics page" element={<Topics />} />
          <Route path="/topicSubmission" name="Topics page" element={<TopicSubmission />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
