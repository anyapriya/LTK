import React, { Component } from 'react';
import './app.css';
import openSocket from 'socket.io-client';
import { Gamestate, Phase, ActionType, CardAction, Action } from './gameState';
import Board from './board/board';
import { Target } from './target';
import { Connecting } from './connecting';

// TODO: extract into .env or similar
const socket = openSocket('http://localhost:5000'); // localhost works for now since we're on the same network

interface State {
  gamestate?: Gamestate;
  myPlayerId?: number;
}

export default class App extends Component<{}, State> {
  constructor(props: any) {
    super(props);
    this.state = {};
    this.componentDidMount = this.componentDidMount.bind(this);
  }

  componentDidMount() {
    socket.on('gamestate', (gamestate: Gamestate) => {
      console.log(gamestate);
      this.setState({
        gamestate: gamestate,
      });
      // Might be easier to convert hands here to add in card action handleClick which can be moved up here
    });

    this.connect();
  }

  private connect = (): void => {
    socket.emit('connect', (playerId: number) => {
      this.setState({ myPlayerId: playerId });
    });
  };

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
    if (
      this.state.gamestate === undefined ||
      this.state.myPlayerId === undefined
    ) {
      return <Connecting myPlayerId={this.state.myPlayerId} />;
    }

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
