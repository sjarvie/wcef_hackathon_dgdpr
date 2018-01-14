import React, { Component } from "react";
import {List, ListItem} from 'material-ui/List';
import Attachment from 'material-ui/svg-icons/file/attachment';

import keypair from 'keypair';
import _ from 'lodash';
import {
  Table,
  TableBody,
  TableFooter,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import RaisedButton from 'material-ui/RaisedButton';

function RecipientList({tableData}) {
  return (
    <Table multiSelectable={false}>
      <TableHeader
        displaySelectAll={false}
        adjustForCheckbox={false}
      >
        <TableRow>
          <TableRowColumn>Recipient Name</TableRowColumn>
          <TableRowColumn>Recipient Public Key</TableRowColumn>
          <TableRowColumn className="grant-revoke"></TableRowColumn>
          <TableRowColumn className="grant-revoke"></TableRowColumn>
        </TableRow>
      </TableHeader>
      <TableBody displayRowCheckbox={false}>
        {
          tableData.map((row, index) => (
            <TableRow key={index}>
              <TableRowColumn>{row.name}</TableRowColumn>
              <TableRowColumn>{row.public_key}</TableRowColumn>
              <TableRowColumn><RaisedButton label="Grant"/></TableRowColumn>
              <TableRowColumn><RaisedButton label="Revoke"/></TableRowColumn>
            </TableRow>
          ))
        }
      </TableBody>
    </Table>
  );
}

export default class UserList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selected_file_id: '',
      recipients: {}
    };
  }

  componentDidMount() {
    this.setState({
      selected_file_id: '',
      recipients: {
        'file_1.pdf': [{
          name: 'Bob',
          public_key: keypair().public
        }],
        'file_2.pdf': [{
          name: 'Charles',
          public_key: keypair().public
        },
          {
            name: 'Bob',
            public_key: keypair().public
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
            recipients[selected_file_id] ? <RecipientList tableData={recipients[selected_file_id]} /> : null
          }
        </div>
      </div>

    );
  }
}
