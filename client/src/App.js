import React, { Component } from 'react';
import './App.css';
import UserList from './UserList'
import Download from './Download'
import AppBar from 'material-ui/AppBar';
import Avatar from 'material-ui/Avatar';
import Button from 'material-ui/RaisedButton';
import {download} from "./api";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      page: null
    }
  }

  render() {
    return (
      <div className="App">
        <AppBar
          title="dGDPR"
          iconElementRight={<Avatar label="alice">A</Avatar>}
        >
        </AppBar>
        <div className="page">
          {
            !this.state.page ? <UserList /> : <Download/>
          }
        </div>
      </div>
    );
  }
}

export default App;
