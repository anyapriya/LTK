import { Target } from "./target";
import { Player } from "./board/player";

export interface Gamestate {
  players: Player[];
  activePlayerId: number;
  turnPlayerId: number;
  currentPhase: Phase;
  activeActions: ActiveAction[];
  possibleActions: Action[];
}

export interface ActiveAction extends Action {
  target?: Target;
  id: number;
}

export interface CardAction extends Action {
  type: ActionType.CARD;
  cardId: number;
}

export interface Action {
  type: ActionType;
  hasTargets: boolean; // If an action targets something, the client will ask the server for possible targets
}

export enum ActionType {
  CARD,
  END_TURN,
  PASS
}

export enum Phase {
  BEGINNING_OF_TURN,
  JUDGEMENT,
  DRAW,
  PLAY,
  DISCARD,
  END_OF_TURN
}