import React, { FunctionComponent } from 'react';
import { Player } from './player';
import Hand from './Hand';
import './playerDisplay.scss';
import { CardAction } from '../gamestate';
import { Target } from '../target';

interface Props {
  player: Player;
  isMe: boolean;
  cardActions?: CardAction[];
  getTargets: (action: CardAction) => Promise<Target[]>;
  performAction: (action: CardAction, target?: Target) => void;
}

const PlayerDisplay: FunctionComponent<Props> = (props) => (
  <div className="playerDisplay">
    <header>{props.player.name}</header>
    {props.isMe ? (
      <Hand
        cards={props.player.hand}
        cardActions={props.cardActions}
        getTargets={props.getTargets}
        performAction={props.performAction}
      />
    ) : (
      <p># of cards in hand: {props.player.hand.length}</p>
    )}
    <p>Health: {props.player.currentHealth} / 4</p>
  </div>
);

export default PlayerDisplay;
