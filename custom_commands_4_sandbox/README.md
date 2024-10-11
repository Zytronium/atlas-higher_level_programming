# Custom Commands

---
This directory cotains executable files  that I made to help in the terminal.
I copied them here so that I can use them in the sandbox. To use these commands,
copy or move them to `/bin`. Then, you can use them the same way as any other
Linux command. 

## dis
- Displays the contents of all given directories or the current directory.
- Then, displays the path of the current working directory.
- You may use any flags that the `ls` command uses. Additionally, there are 2 more flags
  - `-e`: add extra space; surrounding the output in a blank line.
  - `-E`: Don't add the blank line between the dir contents and path
- Useful when navigating around the file system, especially if your terminal\
prompt doesn't display the current path.
- It's the only command here written in C instead of bash.

## cpnxt
- Copies the specified file and changes the copy's name to add 1 to the number at the beginning of the file name. (or sets the number to the value of the last parameter)
- Usage: cpnxt <file path> <new number (optional)>
  - parameter <file path>: The path or file name of the file to copy. The file name must start with a number followed by a '-'.
  - parameter <new number>: (Optional parameter) Number to replace number at beginning of file name. Defaults to specified file's number + 1 if not specified.
- Flags:
  - `--help` basically just shows what's above: how to use the command.
- Note: "cpnxt" is kind of hard to type fast, so it is recommended to set an alias. Perhaps `cn`

## gacp
- Git add, commit, & push
- If an argument is supplied, then that is the commit message.
- The commit message should be in quotes if its more than 1 word.
- If no args are given, it commits with the message "commit msg"

## newpy
- Creates a new executable python script with a shebang in it.
- The fist given argument is the name of the new python file. 
- If a file with the given name already exists, it won't create or overwrite anything.

## xpy
- Adds execute permissions to all files in current directory ending in '.py'

## space
- Prints a large space so you can clear the terminal but still scroll up to see the history
