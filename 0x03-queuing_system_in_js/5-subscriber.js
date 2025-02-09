import { createClient } from 'redis';

const client = createClient();
client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.subscribe('ALXchannel');

client.on('message', (message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('ALXchannel');
    client.quit();
  }
});
