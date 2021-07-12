import React, { useState } from 'react';

function Counter2(props) {
  const [count, setCount] = useState(0);
  return (
    <div>
      <span>you clicked counter {props.id} {count} times</span>
      <button onClick={() => setCount(count + 1)}>
        counter {props.id}
      </button>
    </div>
  );
}

export default Counter2;
