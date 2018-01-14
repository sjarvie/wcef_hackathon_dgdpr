import React, { Component } from "react";
import {List, ListItem} from 'material-ui/List';
import Attachment from 'material-ui/svg-icons/file/attachment';
import _ from 'lodash';
import config from './config';
import * as api from './api';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';

import {
  Table,
  TableBody,
  TableHeader,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import RaisedButton from 'material-ui/RaisedButton';

export class RecipientList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false
    }
  }

  handleGrant({sender, receiver, name, filename, rekey, encryptedEphemeralKey}) {
    return () => {
      this.setState({
        open: true
      })
      // return api.grant({sender, receiver, name, filename, rekey, encryptedEphemeralKey});
    }
  }

  handleRevoke({sender, receiver, filename}) {
    return () => {
      console.log(...arguments);
      return api.revoke({sender, receiver, filename});
    }
  }

  handleClose() {
    this.setState({
      open: false
    })
  }

  render() {
    const { tableData } = this.props;
    const actions = [
      <FlatButton
        label="OK"
        primary={true}
        onClick={() => this.handleClose()}
      />
    ];

    return (
      <div>
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
                  <TableRowColumn>{row.key}</TableRowColumn>
                  <TableRowColumn>
                    <RaisedButton
                      onClick={this.handleGrant({
                        sender: config.alice.pk_b64,
                        receiver: config.bob.pk_b64,
                        name: config.bob.name,
                        filename: this.props.filename,
                        rekey: '',
                        encryptedEphemeralKey: ''
                      })}
                      label="Grant"
                    />
                  </TableRowColumn>
                  <RaisedButton
                    onClick={this.handleRevoke({
                      sender: config.alice.pk_b64,
                      receiver: config.bob.pk_b64,
                      filename: this.props.filename
                    })}
                    label="Revoke"
                    style={{marginTop: 6}}
                  />
                </TableRow>
              ))
            }
          </TableBody>
        </Table>
        <Dialog
          title="Access Granted"
          actions={actions}
          modal={true}
          open={this.state.open}
        >
        </Dialog>
      </div>
    );
  }
}

export default class UserList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selected_file_id: '',
      shares: [
        {
          name: config.bob.name,
          key: config.bob.pk_b64
        }
      ],
      files: [
        'file_123.pdf',
        'file_1234.pdf'
      ]
    };
  }


  componentDidMount() {
    return api.listFiles({
      sender: config.alice.pk_b64
    }).then(response => {
      this.setState({
        // files: _.get(response, 'data.files')
      });
    });
  }

  setPage(filename) {
    return () => {
      return api.getAllShares({
        filename,
        sender: config.alice.pk_b64
      })
      .then(response => {
        this.setState({
          selected_file_id: filename,
          // shares: _.get(response, 'data.shares')
        });
      });
    }
  }

  render() {
    const files = _.get(this.state, 'files', []);
    const shares = _.get(this.state, 'shares');
    const selected_file_id = _.get(this.state, 'selected_file_id', '');

    return (
      <div className="list-page">
        <div className="list">
          <List>
            {
              files.map(fileName => {
                return (
                  <ListItem key={fileName} onClick={this.setPage(fileName)} leftIcon={<Attachment />}>
                    {fileName}
                  </ListItem>
                )
              })
            }
          </List>
        </div>
        <div className="recipients">
          {
            selected_file_id ?
            <RecipientList
              tableData={shares}
              fileName={selected_file_id}
            /> :
            null
          }
        </div>
      </div>

    );
  }
}
