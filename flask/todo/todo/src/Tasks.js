import React from 'react';
import Task from './Task';

class Tasks extends React.Component {
  state = {
    data: []
  };

  handleCompleted = (e, row) => {
    const data = this.state.data;
    for (const task of data) {
      if (task.id == row.id) {
        task.completed = e.target.checked;
      }
    }
    this.setState({data});
  };

  async componentDidMount() {
    try {
      const response = await fetch('/tasks/');
      if (response.status !== 200) {
        throw new Error("http error: " + response.status);
      }
      const data = await response.json();
      this.setState({ data: data.tasks });
    } catch (error) {
      console.log("cannot reach server: " + error);
    }
  }

  render() {
    const tasks = this.state.data;
    const components = tasks.map(task =>
      <li key={task.id}>
        <Task id={task.id}
              description={task.description}
              completed={task.completed}
              onCompletedChange={(e) => this.handleCompleted(e, task)} />
      </li>
    );
    return <ul>{components}</ul>;
  }
}

export default Tasks;
