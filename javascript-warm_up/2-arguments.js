#!/usr/bin/node

console.log((() => {
    switch (process.argv.length) {
        // length is always >= 2 because index 0 & 1 are given automatically.
        case 2:
            return 'No arguments';

        case 3:
            return 'Argument found';

        default:
            return 'Arguments found';
    }
})())
