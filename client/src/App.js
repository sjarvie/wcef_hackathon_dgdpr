import React, { Component } from 'react';
import './App.css';
import UserList from './UserList'
import AppBar from 'material-ui/AppBar';
import Avatar from 'material-ui/Avatar';

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="App">
        <AppBar
          title="dGDPR"
          iconElementRight={<Avatar label="alice">A</Avatar>}
        />
        <div className="page">
          <UserList />
        </div>
      </div>
    );
  }
}

export default App;
