import React from 'react';

class Counter extends React.Component {
  state = {
    count: 0
  }

  handleClick = () => {
    this.setState(prevState => ({count: prevState.count + 1}));
  }

  render() {
    return (
      <div>
        count: {this.state.count}
        <button onClick={this.handleClick}>click me!</button>
      </div>
    );
  }
}

export default Counter;
