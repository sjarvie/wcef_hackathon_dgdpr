import React, { Component } from 'react';
import './App.css';
import Upload from './Upload';
import UserList from './UserList'
import Menu from 'material-ui/Menu';
import MenuItem from 'material-ui/MenuItem';
import AppBar from 'material-ui/AppBar';
import FlatButton from 'material-ui/FlatButton';
import Avatar from 'material-ui/Avatar';

const routes = {
  upload: <Upload />,
  list: <UserList/>
};

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      current_page: 'upload'
    };
  }

  setPage(pageName) {
    this.setState({
      current_page: pageName
    });
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
