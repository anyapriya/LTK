import React, { FunctionComponent } from 'react';

interface Props {
  cards: string[];
}

const Hand: FunctionComponent<Props> = props => (
  <React.Fragment>
    <div>Hand</div>
    <ul>
      {props.cards.map((card, index) => (
        <li key={index}>
          {card}
        </li>
      ))}
    </ul>
  </React.Fragment>
);

export default Hand;