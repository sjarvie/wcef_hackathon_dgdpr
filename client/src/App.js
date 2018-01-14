import React, { Component } from 'react';
import './App.css';
import Upload from './Upload';
import UserList from './UserList'
import Menu from 'material-ui/Menu';
import MenuItem from 'material-ui/MenuItem';

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
        <header className="App-header">
          <h1 className="App-title">dGDPR</h1>
        </header>
        <div className="menu">
          <Menu selectedMenuItemStyle={{backgroundColor: 'red'}}>
            <MenuItem onClick={() => this.setPage('upload')} primaryText="Upload" />
            <MenuItem onClick={() => this.setPage('list')} primaryText="My Files" />
          </Menu>
        </div>
        <div className="page">
          {routes[this.state.current_page]}
        </div>
      </div>
    );
  }
}

export default App;
