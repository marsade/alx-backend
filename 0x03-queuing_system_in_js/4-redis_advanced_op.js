import { createClient, print } from 'redis';

const client = createClient();
client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.HSET('ALX', 'Portland', '50', print);
client.HSET('ALX', 'Seattle', '80', print);
client.HSET('ALX', 'New York', '20', print);
client.HSET('ALX', 'Bogota', '20', print);
client.HSET('ALX', 'Cali', '40', print);
client.HSET('ALX', 'Paris', '2', print);

client.HGETALL('ALX', (err, result) => {
  if (err) throw err;
  console.log(result);
});
