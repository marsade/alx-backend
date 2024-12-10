const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phonenumber, message, done) {
  console.log(`Sending notification to ${phonenumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code', function(job, done) {
  sendNotification(job.data.phonenumber, job.data.message, done);
});