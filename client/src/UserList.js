import React, { Component } from "react";
import {List, ListItem} from 'material-ui/List';
import Attachment from 'material-ui/svg-icons/file/attachment';
import _ from 'lodash';
import config from './config';
import * as api from './api';

import {
  Table,
  TableBody,
  TableHeader,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import RaisedButton from 'material-ui/RaisedButton';

export class RecipientList extends Component {
  handleGrant({sender, receiver, name, filename, rekey, encryptedEphemeralKey}) {
    return () => {
      return api.grant({sender, receiver, name, filename, rekey, encryptedEphemeralKey});
    }
  }

  handleRevoke({sender, receiver, filename}) {
    return () => {
      return api.revoke({sender, receiver, filename});
    }
  }

  render() {
    const { tableData } = this.props;
    return (
      <Table multiSelectable={false}>
        <TableHeader
          displaySelectAll={false}
          adjustForCheckbox={false}
        >
          <TableRow>
            <TableRowColumn>Recipient Name</TableRowColumn>
            <TableRowColumn>Recipient Public Key</TableRowColumn>
            <TableRowColumn></TableRowColumn>
            <TableRowColumn></TableRowColumn>
          </TableRow>
        </TableHeader>
        <TableBody displayRowCheckbox={false}>
          {
            tableData.map((row, index) => (
              <TableRow key={index}>
                <TableRowColumn>{row.name}</TableRowColumn>
                <TableRowColumn>{row.public_key}</TableRowColumn>
                <TableRowColumn>
                  <RaisedButton
                    onClick={this.handleGrant({
                      sender: config.alice.pk_b64,
                      receiver: config.bob.pk_b64,
                      name: config.bob.name,
                      filename: this.props.filename,
                      rekey
                    })}
                    label="Grant"
                  />
                </TableRowColumn>
                <TableRowColumn>
                  <RaisedButton onClick={this.handleRevoke} label="Revoke"/>
                </TableRowColumn>
              </TableRow>
            ))
          }
        </TableBody>
      </Table>
    );
  }
}

export default class UserList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selected_file_id: '',
      recipients: {},
      files: []
    };
  }


  componentDidMount() {
    this.setState({
      selected_file_id: '',

      recipients: {
        'file_1.pdf': [{
          name: 'Bob',
          public_key: config.bob.pk_b64
        }],
        'file_2.pdf': [
          {
            name: 'Bob',
            public_key: config.bob.pk_b64
          }]
      }
    });
  }

  setPage(fileName) {
    this.setState({
      selected_file_id: fileName
    });
  }

  render() {
    const recipients = _.get(this.state, 'recipients', {});
    const selected_file_id = _.get(this.state, 'selected_file_id', '');

    return (
      <div className="list-page">
        <div className="list">
          <List>
            {
              _.keys(recipients).map(fileName => {
                return (
                  <ListItem key={fileName} onClick={() => this.setPage(fileName)} leftIcon={<Attachment />}>
                    {fileName}
                  </ListItem>
                )
              })
            }
          </List>
        </div>
        <div className="recipients">
          {
            recipients[selected_file_id] ?
            <RecipientList
              tableData={recipients[selected_file_id]}
              fileName={selected_file_id}
            /> :
            null
          }
        </div>
      </div>

    );
  }
}
