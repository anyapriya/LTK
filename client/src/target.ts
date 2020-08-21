export interface PlayerTarget extends Target {
  type: TargetType.PLAYER;
  id: number;
}

export interface ActiveActionTarget extends Target {
  type: TargetType.ACTIVE_ACTION;
  id: number;
}

export interface Target {
  type: TargetType;
}

export enum TargetType {
  PLAYER = 'PLAYER',
  ACTIVE_ACTION = 'ACTIVE_ACTION',
}
