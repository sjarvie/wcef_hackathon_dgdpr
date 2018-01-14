import React, { Component } from "react";
import {List, ListItem} from 'material-ui/List';
import Attachment from 'material-ui/svg-icons/file/attachment';
import Avatar from 'material-ui/Avatar';

export default class UserList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      selected_file: ''
    }
  }

  render() {
    return (
      <div className="list-page">
        <div className="list">
          <List>
            <ListItem leftIcon={<Attachment />}>
              Colonoscopy_Results.pdf
            </ListItem>
            <ListItem leftIcon={<Attachment />}>
              Stool_test_results.pdf
            </ListItem>
          </List>
        </div>
        <div className="recipients">
          <List>
            <ListItem rightIcon={<Avatar label="alice">B</Avatar>}>
              Bob
            </ListItem>
            <ListItem rightIcon={<Avatar label="alice">C</Avatar>}>
              Charles
            </ListItem>
          </List>
        </div>
      </div>

    );
  }
}