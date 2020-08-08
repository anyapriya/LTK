import React, { FunctionComponent } from 'react';
import { Player } from './player';
import PlayerDisplay from './PlayerDisplay';
import { CardAction } from '../gamestate';
import { Target } from '../target';

interface Props {
  // Is splitting these up by otherPlayers and myPlayer easier?
  players: Player[];
  myPlayerId: number;
  cardActions: CardAction[];
  getTargets: (action: CardAction) => Promise<Target[]>;
  performAction: (action: CardAction, target?: Target) => void;
}

const Board: FunctionComponent<Props> = props => (
  <React.Fragment>
    {
      props.players.map((player, index) => {
        return <PlayerDisplay
          key={index}
          player={player}
          isMe={index === props.myPlayerId}
          cardActions={props.cardActions}
          getTargets={props.getTargets}
          performAction={props.performAction}/>
      })
    }
  </React.Fragment>
);

export default Board;