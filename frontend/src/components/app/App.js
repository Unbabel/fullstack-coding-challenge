import React from 'react';
import Header from '../header/Header';

const app = () => {
  return(
    <div className="App">
      <Header></Header>
      <header className="App-header">
        <p>
          Edit <code>src/app.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default app;
