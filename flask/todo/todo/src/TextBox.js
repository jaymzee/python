import React from 'react'

function TextBox(props) {
  const [name, setName] = React.useState('');
  return (
    <div>
      <input type="text"
             onChange={(e) => setName(e.target.value)}
             value={name}
      />
    </div>
  );
}

export default TextBox;
