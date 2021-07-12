import logo from './logo.svg';
import './App.css';
import Tasks from './Tasks';
import CounterContainer from './CounterContainer';
import TextBox from './TextBox';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <div align="left">
          <Tasks />
        </div>
        <CounterContainer initialCount={ 1 } />
        <TextBox />
      </header>
    </div>
  );
}

export default App;
