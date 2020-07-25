import * as React from 'react';

interface State {
  cards: string[];
}

const initialState: State = {
  cards: ['Strike', 'Strike', 'Dodge', 'Peach', 'Dismantle']
}

export default class Hand extends React.Component<{}, State> {
  state: State = initialState;

  render() {
    return (
      <React.Fragment>
        <div>Hand</div>
        <ul>
          {this.state.cards.map((card, index) => (
            <li key={index}>
              {card}
            </li>
          ))}
        </ul>
      </React.Fragment>
    )
  }
}