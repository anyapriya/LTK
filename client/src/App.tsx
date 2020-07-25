import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Hand from './board/Hand';
import { w3cwebsocket as W3CWebSocket } from 'websocket';

const client = new W3CWebSocket('ws://127.0.0.1:8000');

class App extends Component {

  componentWillMount() {
    client.onopen = () => {
      console.log('Websocket connected');
    }

    client.onmessage = (message) => {
      console.log(message);
    }
  }

  render() {
    return (
      <div className="App">
        <button onClick={() => client.send("Testing")}>Send Message</button>
        <Hand/>
      </div>
    );
  }
}

export default App;
