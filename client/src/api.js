import axios from 'axios';
const config = './config';

const instance = axios.create({
  baseURL: config.base_url,
  timeout: 1000,
  headers: {'Content-Type': 'application/json'}
});

export function listFiles({sender}) {
  return instance.get('/files', { params: { sender }})
  .catch(function (error) {
    console.log(error);
  });
}

export function getAllShares({sender, filename}) {
  return instance.get('/shares', {
    params: {
      sender, filename
    }})
  .catch(function (error) {
    console.log(error);
  });
}

export function grant({sender, receiver, name, filename, rekey, encryptedEphemeralKey}) {
  return instance.post('/shares', {
    sender, receiver, name, filename, rekey, encryptedEphemeralKey
  })
  .catch(function (error) {
    console.log(error);
  });
}

export function revoke({sender, receiver, filename}) {
  return instance.delete('/shares', {
    params: {
      sender, receiver, filename
    }
  })
  .catch(function (error) {
    console.log(error);
  });
}

export function upload({filename, cyphertext, edek, sender}) {
  return instance.post('/upload/', {
    filename, cyphertext, edek, sender
  })
  .catch(function (error) {
    console.log(error);
  });
}

export function download({}) {

}