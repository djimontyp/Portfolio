import React from 'react';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <div id="lead">
        <div id="lead-content">
          <img src="/myself3.jpg" className="MySelf"
               alt="djimontyp (Maks Naumenko)"></img>
          <div id="names">
            <h1>Maks Naumenko</h1>
            <strong><a
              href="https://twitter.com/djimontyp"
              rel="noopener"
              className="text-green-600 text-3xl"
            >@djimontyp</a></strong>
          <h2>Software Engineer</h2>
          </div>
        </div>
        <div id="lead-overlay"></div>
      </div>
      <div id="about-me"><br/><br/><br/><br/></div>
    </div>

  );
}

export default App;
