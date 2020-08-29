import React, { Component } from 'react';
import './app.css';
import openSocket from 'socket.io-client';
import { Gamestate, Phase, ActionType, CardAction, Action } from './gameState';
import { CardType } from './board/player';
import Board from './board/board';
import { Target } from './target';

// TODO: extract into .env or similar
const socket = openSocket('http://localhost:5000'); // localhost works for now since we're on the same network

interface State {
  gamestate: Gamestate;
  myPlayerId: number;
}

const initialGamestate: Gamestate = {
  players: [
    {
      id: 0,
      name: 'P1',
      currentHealth: 3,
      hand: [CardType.STRIKE, CardType.STRIKE, CardType.PEACH, CardType.DODGE],
    },
    {
      id: 1,
      name: 'P2',
      currentHealth: 3,
      hand: [],
    },
    {
      id: 2,
      name: 'P3',
      currentHealth: 2,
      hand: [CardType.DODGE, CardType.DODGE],
    },
    {
      id: 3,
      name: 'P4',
      currentHealth: 0,
      hand: [],
      dead: true,
    },
  ],
  activePlayerId: 0,
  turnPlayerId: 0,
  currentPhase: Phase.PLAY,
  activeActions: [],
  possibleActions: [
    {
      type: ActionType.CARD,
      cardId: 0,
      hasTargets: true,
    } as CardAction,
    {
      type: ActionType.CARD,
      cardId: 1,
      hasTargets: true,
    } as CardAction,
    {
      type: ActionType.CARD,
      cardId: 2,
      hasTargets: false,
    } as CardAction,
    {
      type: ActionType.END_TURN,
      hasTargets: false,
    },
  ],
};

export default class App extends Component<{}, State> {
  constructor(props: any) {
    super(props);
    this.state = {
      gamestate: initialGamestate,
      myPlayerId: 0, // TODO: Remove once we're actually connecting to the server
    };

    this.componentDidMount = this.componentDidMount.bind(this);
  }

  componentDidMount() {
    socket.on('connect', () => {
      console.log('Websocket connected');
    });

    socket.on('message', (message: string) => {
      console.log(message);
    });

    socket.on('gamestate', (gamestate: Gamestate) => {
      console.log(gamestate);
      this.setState({
        gamestate: gamestate,
      });
      // Might be easier to convert hands here to add in card action handleClick which can be moved up here
    });
  }

  // Do we really need to send the full Action, or can we just send the index of the action?
  private getTargets = async (action: Action): Promise<Target[]> => {
    return new Promise((resolve: any) => {
      socket.emit('getTargets', { action }, (response: any) => {
        console.log(response);
        console.log(response.result);
        // TODO: handle error (response.error?)
        return resolve(response.result);
      });
    });
  };

  private performAction = (action: Action, target?: Target) => {
    const body = {
      action,
      ...(target !== undefined && { target }),
    };
    socket.emit('action', body);
  };

  private passPriority = () => {
    this.performAction({
      type: ActionType.PASS,
      hasTargets: false,
    });
  };

  private endTurn = () => {
    this.performAction({
      type: ActionType.END_TURN,
      hasTargets: false,
    });
  };

  private changeMyPlayerId = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newId: number = Number(event.target.value);
    console.log(newId);
    this.setState({
      myPlayerId: newId,
    });
  };

  render() {
    const cardActions: CardAction[] = this.state.gamestate.possibleActions
      .filter((a) => a.type === ActionType.CARD)
      .map((a) => a as CardAction);

    const playerHasPriority =
      this.state.myPlayerId === this.state.gamestate.activePlayerId;
    const passButtonEnabled =
      playerHasPriority &&
      this.state.gamestate.possibleActions.some(
        (a: Action) => a.type === ActionType.PASS
      );
    const endTurnButtonEnabled =
      playerHasPriority &&
      this.state.gamestate.possibleActions.some(
        (a: Action) => a.type === ActionType.END_TURN
      );
    return (
      <React.Fragment>
        <Board
          players={this.state.gamestate.players}
          myPlayerId={this.state.myPlayerId}
          cardActions={cardActions}
          getTargets={this.getTargets}
          performAction={this.performAction}
        />
        <label htmlFor="playerNumberInput">Player #</label>
        <input
          id="playerNumberInput"
          title="Player #"
          type="number"
          onChange={this.changeMyPlayerId}
          defaultValue={0}
        />
        <br />
        {this.state.myPlayerId === this.state.gamestate.activePlayerId
          ? 'You Have Priority'
          : `Player ${this.state.gamestate.activePlayerId} has priority`}
        <br />
        {this.state.myPlayerId === this.state.gamestate.turnPlayerId
          ? 'It is your turn'
          : `It is Player ${this.state.gamestate.activePlayerId}'s turn`}
        <br />
        The current phase is {Phase[this.state.gamestate.currentPhase]}
        <br />
        <button
          disabled={!passButtonEnabled}
          onClick={() => this.passPriority()}>
          PASS
        </button>
        <button disabled={!endTurnButtonEnabled} onClick={() => this.endTurn()}>
          END TURN
        </button>
      </React.Fragment>
    );
  }
}
