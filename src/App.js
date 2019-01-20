import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MiniDrawer from './components/MiniDrawer'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
          <MiniDrawer/>
        </header>
      </div>
    );
  }
}

export default App;
