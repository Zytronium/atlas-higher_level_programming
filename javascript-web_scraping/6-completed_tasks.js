#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err); // log error if request fails
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    // iterate over all tasks and count completed ones by user
    tasks.forEach(task => {
      if (task.completed) { // check if this task is completed
        // if this user ID is not already in the object, add it with a default value of 0
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        // increment number of tasks completed for this user
        completedTasks[task.userId]++;
      }
    });
    // print the results
    console.log(completedTasks);
  }
});
