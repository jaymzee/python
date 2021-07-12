import React from 'react';

export default CounterChild;

function CounterChild({count, dispatch}) {
  return (
    <div>
      <span>count: { count } </span>
      <button onClick={ () => dispatch({ type: 'INCREMENT' }) }>+</button>
      <button onClick={ () => dispatch({ type: 'DECREMENT' }) }>-</button>
    </div>
  );
}
