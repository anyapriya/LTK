import { Player } from "./board/Player";

export interface GameState {
  players: Player[];
  activeActions: Action[];
  possibleActions: Action[];
  activePlayerId: number;
  // gameOver and who won
  currentTurn: number;
  currentPhase: Phase;
}

export interface HandCard {
  actions: Action[];
}

export interface HeroAbility {
  actions: Action[];
}

export interface Action {
  legal: boolean;
  targets: Target[];
}

export interface Target {
  playerId: number;
  id: number;
  // ???
}

export enum Phase {
  BEGINNING_OF_TURN,
  JUDGEMENT,
  DRAW,
  PLAY,
  DISCARD,
  END_OF_TURN
}