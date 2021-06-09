import React from 'react';

class Task extends React.Component {
  render() {
    return <span>Task!: {this.props.description} <input type="checkbox" checked={this.props.completed} onChange={this.props.onCompletedChange} /></span>;
  }
}

export default Task;
