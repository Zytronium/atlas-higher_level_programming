# JavaScript - Objects, Scopes and Closures

---
This project covers more beginner concepts of JavaScript: objects, scopes, and closures.

An object is pretty much anything that exists, like a variable or an instance of a class.


The scope is determined by where in the code something is happening, and determines things
like what can be accessed. Imagine a small file system organized in the following manner:
the Root folder contains FolderA, FolderB, File1, File2, and File3. FolderA contains FolderA1,
FolderA2, FolderA3, FileA1 and FileA2; FolderB contains the same thing but replacing A with B,
and so on. Think of each file as an object, each folder as a function, and the Root folder as
the global scope. Here, you can only access what's in this folder, but usually not what's in
its subfolders unless you open those subfolders. And in one of the subfolders, say FolderA
for example, the scope also includes Root. (Of course that's now how file systems actually
work.) So from FolderA1, you can access FileA1-1, as well as FileA1 and File1, but not FileB1. 

`this` refers to 'this' scope, aka the current scope where `this` is being used.

A closure allows you to access something that is outside the current scope. In the file
system analogy, think of a closure as a syslink or a shortcut to another file.