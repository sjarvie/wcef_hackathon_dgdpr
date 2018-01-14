const config = 'config';
import axios from 'axios';

const instance = axios.create({
  baseURL: config.base_url,
  timeout: 1000,
  headers: {'Content-Type': 'application/json'}
});

export function listFiles(userId) {
  return instance.get(`/list_files/${userId}`)
  .catch(function (error) {
    console.log(error);
  });
}
