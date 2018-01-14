import React, { Component } from "react";
import {List, ListItem} from 'material-ui/List';
import Attachment from 'material-ui/svg-icons/file/attachment';

export default class UserList extends Component {
  render() {
    return (
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
    );
  }
}