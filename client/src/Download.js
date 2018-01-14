import React, { Component } from "react";
import RaisedButton from 'material-ui/RaisedButton';

export default class Download extends Component {
  
  render() {
    return (<div className="upload-page">
      <RaisedButton
        containerElement='label'
        label='Download'>
      </RaisedButton>
    </div>);
  }
}
