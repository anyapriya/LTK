export interface Hero {
  id: number;
  name: string;
  description: string;
  maxHealth: number;
  gender: Gender;
  kingdom: Kingdom;
}

export enum Gender {
  FEMALE,
  MALE
}

export enum Kingdom {
  WU,
  SHU,
  WEI,
  NEUTRAL
}