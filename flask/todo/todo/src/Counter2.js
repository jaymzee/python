import React from 'react';

function Counter2(props) {
  const [count1, setCount1] = React.useState(0);
  const [count2, setCount2] = React.useState(0);
  return (
    <div>
      <p>you clicked counter 1 {count1} times</p>
      <p>you clicked counter 2 {count2} times</p>
      <button onClick={() => setCount1(count1 + 1)}>counter 1</button>
      <button onClick={() => setCount2(count2 + 1)}>counter 2</button>
    </div>
  );
}

export default Counter2;
