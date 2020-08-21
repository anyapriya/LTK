import React, { FunctionComponent, Component } from 'react';
import { CardType } from './player';
import { CardAction } from '../gamestate';
import { Target } from '../target';

interface Props {
  cards: CardType[];
  cardActions?: CardAction[];
  getTargets: (action: CardAction) => Promise<Target[]>;
  performAction: (action: CardAction, target?: Target) => void;
}

export default class Hand extends Component<Props, {}> {

  // Could be nicer if this was handled in App or Board to avoid passing it all the way up the chain (lift the state)
  private handleClick = async (cardId: number) => {
    if (!this.props.cardActions) {
      return;
    }

    // TODO: prevent the user from clicking a different card until the current click is resolved

    const actions: CardAction[] = this.props.cardActions?.filter(a => a.cardId === cardId);

    if (actions.length === 0) {
      return;
    }
    
    // TODO: Prompt the user for which action they're activating (if applicable)
    const action: CardAction = actions[0];
    
    // If the action has targets, get them from the server
    if (action.hasTargets) {
      this.props.getTargets(action).then(
        (targets: Target[]) => {
          // TODO: If there are multiple targets, prompt the user for their choice (modal?)
          const target: Target = targets[0];

          // send server chosen action (and optionally target)
          this.props.performAction(action, target);
        },
        (error) => {
          // handle error?
          console.log(error);
        }
      )
    } else {
      this.props.performAction(action);
    }

  }

  render() {
    return (
      <React.Fragment>
        <div>Hand</div>
        {this.props.cards.length > 0 &&
          <ul>
            {this.props.cards.map((card, index) => (
              <HandCard
                key={index}
                id={index}
                cardName={CardType[card]}
                onClick={() => this.handleClick(index)}/>
            ))}
          </ul>
        }
        {this.props.cards.length === 0 && "No cards in hand"}
      </React.Fragment>
    );
  }
}


interface HandCardProps {
  id: number;
  cardName: string;
  onClick: any; // onClick should only exist if the card has a possible action
}

const HandCard: FunctionComponent<HandCardProps> = props => (
  <li key={props.id} onClick={props.onClick}>
    {props.cardName}
  </li>
)