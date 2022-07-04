import React from 'react';
import './styles/App.css';
import SocialFlow from "./components/SocialFlow";

function App() {
  return (
    <div className="App">
      <div id="lead">
        <div id="lead-content">
          <div id="names">
            <h1>Hey! I'm Maks Naumenko - Software Engineer.</h1>
            <strong><a
              href="https://github.com/djimontyp"
              rel="noopener"
              className="text-green-600 text-3xl"
            >@djimontyp</a></strong>
          </div>
          <SocialFlow/>
        </div>
        <div id="lead-overlay"></div>
      </div>
      <div id="about-me"></div>
    </div>
  );
}

export default App;
