import React, { Component } from "react";
import RaisedButton from 'material-ui/RaisedButton';

export default class Upload extends Component {
  render() {
    return (<div className="upload-page">
      <input type="file"/>
      <RaisedButton label="Upload" />
    </div>);
  }
}
