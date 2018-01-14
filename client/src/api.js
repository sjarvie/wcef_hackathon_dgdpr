const config = 'config';
import axios from 'axios';

const instance = axios.create({
  baseURL: config.base_url,
  timeout: 1000,
  headers: {'Content-Type': 'application/json'}
});

export function getAllShares({sender}) {
  return instance.get('/files', {params: { sender }})
  .catch(function (error) {
    console.log(error);
  });
}

export function getShare({sender, filename}) {
  return instance.get('/shares', {
    params: {
      sender, filename
    }})
  .catch(function (error) {
    console.log(error);
  });
}

