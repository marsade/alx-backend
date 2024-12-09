import { createClient, print } from 'redis';
import { promisify } from 'util'

const client = createClient();
client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const schoolValue = await getAsync(schoolName);
    console.log(schoolValue);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}:`, err);
  }
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');