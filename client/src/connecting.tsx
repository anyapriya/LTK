import React, { FunctionComponent } from 'react';

interface Props {
  myPlayerId?: number;
}

export const Connecting: FunctionComponent<Props> = (props) => (
  <React.Fragment>
    <h1>
      Connecting to Lobby
      {props.myPlayerId !== undefined && ` as Player ${props.myPlayerId}`}
    </h1>
  </React.Fragment>
);
