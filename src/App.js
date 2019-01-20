import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import SideMenu from "./components/SideMenu";
import Console from "./components/Console";
import Status from "./components/Status";
import Button from "@material-ui/core/Button";
import Window from "./components/CodeStuff/Window";
import WeirdFlex from "./components/WeirdFlex";
import Text from "./components/Text";
import { withStyles } from "@material-ui/core/styles";
import Butt from "./components/CodeStuff/heckin_button";
import axios from "axios";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <link
            rel="stylesheet"
            href="https://fonts.googleapis.com/css?family=Roboto:300,400,500"
          />
          <link
            rel="stylesheet"
            href="https://fonts.googleapis.com/icon?family=Material+Icons"
          />

          <textarea
            id="HELLO"
            rows="20"
            cols="150"
            style={{
              background: "url(http://i.imgur.com/2cOaJ.png)",
              "background-attachment": "local",
              "background-repeat": "no-repeat",
              "padding-left": "35px",
              "padding-top": "10px",
              "border-color": "#ccc",
              color: "white",
              height: "100 vw",
              position: "absolute",
              left: 0,
              bottom: 0
            }}
          />
          <Butt
            onClick={() => {
              axios
                .post("http://35.233.140.84:80/", "MV 1 $A")
                .then(res => console.log(res))
                .catch(reeeeeeee => console.log(reeeeeeee));
            }}
          >
            Check Code
          </Butt>
          <SideMenu />
        </header>
      </div>
    );
  }
}

export default App;
