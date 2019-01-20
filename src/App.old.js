import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import SideMenu from "./components/SideMenu";
import Console from "./components/Console";

class App extends Component {
  render() {
    const divStyle = {
      "margin-top": "100%"
    };

    const bottomStyle = {
      position: "absolute",
      bottom: 0,
      left: 0,
      border: "dotted 3px red"
    };

    const vsplit = {
      display: "inline-block",
      width: "40%",
      height: "100vw",
      border: "dotted 3px green"
    };
    const hsplit = {
      border: "dotted 3px blue",
      width: "40%",
      height: "100%"
    };

    return (
      <div>
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Roboto:300,400,500"
        />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/icon?family=Material+Icons"
        />
        <div style={vsplit}>
          <div style={hsplit}>Menu 2</div>
          <div style={hsplit}>
            <div style={vsplit}> 3 </div>
            <div style={vsplit}> 4 </div>
          </div>
        </div>
        <div style={vsplit}> sideMenu 1</div>
      </div>
    );
  }
}

export default App;
