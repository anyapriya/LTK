export interface Card {
  name: string;
  description: string;
  suit: Suit;
  number: number;
}

export enum Suit {
  SPADES,
  HEARTS,
  CLUBS,
  DIAMONDS
}

export interface Weapon extends Card {
  range: number;
}
