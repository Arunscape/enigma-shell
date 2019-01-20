import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MiniDrawer from './components/MiniDrawer'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <MiniDrawer/>
        </header>
      </div>
    );
  }
}

export default App;
