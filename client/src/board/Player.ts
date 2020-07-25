import { Card, Weapon } from "./Card";
import { Hero } from "./Hero";

export interface Player {
  id: number; // represents position on the board
  name: string;
  hero: Hero;
  currentHealth: number;
  equipment: EquippedItems;
  handSize: number;
  role?: Role;
  hand?: Card[];
}

export enum Role {
  MONARCH,
  MINISTER,
  REBEL,
  TURNCOAT
}

export interface EquippedItems {
  weapon?: Weapon;
  armor?: Card;
  horseOffensive?: Card;
  horseDefensive?: Card;
}
