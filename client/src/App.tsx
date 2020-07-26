import React, { Component } from 'react';
import './App.css';
import Hand from './board/Hand';
import openSocket from 'socket.io-client';

const socket = openSocket('http://localhost:5000'); // Works for now since we're on the same network

interface State {
  cards: string[];
}

export default class App extends Component<{}, State> {
  constructor(props: any) {
    super(props);
    this.state = {
      cards: []
    }

    this.componentDidMount = this.componentDidMount.bind(this);
  }
  
  componentDidMount() {
    socket.on('connect', () => {
      console.log('Websocket connected');
    });

    socket.on('message', (message: string) => {
      console.log(message);
    });

    socket.on('gamestate', (data: string[]) => {
      console.log(data);
      this.setState({
        cards: data
      });
    });
  }

  shuffleHand() {
    socket.emit('shuffle_hand');
  }

  render() {
    const nCards = this.state.cards.length;
    return (
      <div className="App">
        {nCards > 0 &&
          <div className="Player">
            <button onClick={() => this.shuffleHand()}>Shuffle Hand</button>
            <Hand cards={this.state.cards}/>
          </div>
        }
      </div>
    );
  }
}
