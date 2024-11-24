#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
      const tasks = JSON.parse(body);
      const completedTasks = tasks.forEach(task => {
          if (task.completed) {
              if (!this[task.userId]) {
                  this[task.userId] = 0;
              }
              this[task.userId]++;
          }
      });
      console.log(completedTasks);
  }
});
