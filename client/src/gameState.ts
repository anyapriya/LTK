import { Target } from './target';
import { Player } from './board/player';

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
  cardId?: number; // Should this be required? Does it make sense for an active card action to have a cardId?
}

export interface Action {
  type: ActionType;
  hasTargets: boolean; // If an action targets something, the client will ask the server for possible targets
}

export enum ActionType {
  CARD = 'CARD',
  END_TURN = 'END_TURN',
  PASS = 'PASS',
  DEATHS_DOOR = 'DEATHS_DOOR',
}

export enum Phase {
  BEGINNING_OF_TURN = 'BEGINNING_OF_TURN',
  JUDGEMENT = 'JUDGEMENT',
  DRAW = 'DRAW',
  PLAY = 'PLAY',
  DISCARD = 'DISCARD',
  END_OF_TURN = 'END_OF_TURN',
}
