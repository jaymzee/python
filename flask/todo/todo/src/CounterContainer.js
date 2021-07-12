import React, { useReducer } from 'react';
import PropTypes from 'prop-types';
import Counter from './Counter';

export default CounterContainer;

function init(initialCount) {
  console.log('initialCount:', initialCount);
  return { count: initialCount };
}

function reducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 }
    case 'DECREMENT':
      if (state.count > 0) {
        return { count: state.count - 1 }
      } else {
        return state;
      }
    default:
      throw new Error('invalid action type');
  }
}

function CounterContainer({initialCount}) {
  const [state, dispatch] = useReducer(reducer, initialCount, init);
  return <Counter count={ state.count }
                  dispatch={ dispatch } />
}

CounterContainer.propTypes = {
  initialCount: PropTypes.number.isRequired
}
