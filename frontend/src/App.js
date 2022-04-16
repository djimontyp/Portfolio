import React from 'react';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <div id="lead">
        <div id="lead-content">
          <div id="names">
            <h1>Maks Naumenko</h1>
            <strong><a
              href="https://twitter.com/djimontyp"
              target="_blank"
              rel="noopener"
              className="text-green-600 text-3xl"
            >@djimontyp</a></strong>
          </div>
          <h2>Software Engineer</h2>
        </div>
        <div id="lead-overlay"></div>
      </div>
      <div id="about-me"><br/><br/><br/><br/></div>
    </div>
  );
}

export default App;
