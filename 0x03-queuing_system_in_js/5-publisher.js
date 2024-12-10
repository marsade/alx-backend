import { createClient } from 'redis';

const client = createClient();
client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function publishMessage(message, timer) {
  setTimeout(() => {
    console.log('About to send message: ', message);
    client.publish('ALXchannel', message);
  }, timer);
}

publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
