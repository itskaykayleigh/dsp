# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

Result | Command Line
------ | ------------ 
show current working directory path | pwd 
creating a directory | mkdir directory_name 
deleting a directory | rm -r dirctory_name 
creating a file using `touch` command | touch filename 
deleting a file | rm filename 
renaming a file | mv filename_original filename_renamed
listing hidden files | ls -a 
copying a file from one directory to another | cp directory1/filename directory2/
list all files of current directory | ls 
switch directory | cd 
move a file to a directory | mv filename directory/

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

Command Line | Result 
------------ | ------
ls | list all files of current directory
ls -a | list all contents, including hidden files and directories
ls -l | list all contents in long format 
ls -lh | list long format with readable file size
ls -lah | list long format with readable file size including hidden files
ls -t | sort by time & date lastly modified 
ls -Glp | list long format with no owner (only group ID) and puts \ after directory name  
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -d  
ls -t  
ls -a  
ls -l  
ls -r   
ls -X  
ls ~ 

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

It executes argument. Specifically, it reads data from standard input (stdin) and executes the command (supplied to it as argument) one or more times based on the input read. Any blanks and spaces in input are treated as delimiters, while blank lines are ignored. And 
If no command is supplied as argument to xargs, the default command that the tool executes is echo. 

Examples to use: 
 * xargs find -name "*.txt"  
 pass the find command along with its option "-name" as argument to xargs, and provide "*.txt" as input through stdin  ` 
`--> The command will search all .txt files in the working directory` 

 

