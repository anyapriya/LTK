export interface Player {
  id: number; // represents position on the board
  name: string;
  currentHealth: number;
  hand: CardType[];
  dead?: boolean; // true when the player is completely out of the game
}

export enum CardType {
  STRIKE = 'STRIKE',
  DODGE = 'DODGE',
  PEACH = 'PEACH'
}