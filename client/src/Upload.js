import React, { Component } from "react";
import RaisedButton from 'material-ui/RaisedButton';

export default class Receiver extends Component {
  render() {
    return (<div className="upload-page">
      <RaisedButton
        containerElement='label'
        label='Upload'>
        <input type="file" />
      </RaisedButton>
    </div>);
  }
}
