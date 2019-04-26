ALL files, other than start.html and project.sh, must go in the /usr/lib/cgi-bin/ directory. The start.html file must similarly be moved to /var/www/html/ for the program to work. project.sh can be placed anywhere the user desires.

To run the program, the user must simply run the project.sh file. Instructions for using Nikolai's features will be found on the HTML page once the user presses "start" on the initial page.

The only feature with a degree of "complexity" to it is the calculator feature (option 7). Although the instructions are noted in the HTML page like normal, an error will occur if these instructions are not followed carefully. 

Example: button 7, load, button 3, button 4, button 2, button 1, button plus, button 1, button 2, button EQ would be the correct way to do   3421 + 12 in the calculator. Had the user put another plus right before pressing EQ, an error would occur.

To "power off" Nikolai, press the power button. The program does not technically stop at this point, but it will not take button input except for the power button. Pressing the power button will power it back on and resume the program as normal.

To exit the program, simply ctrl-c or click exit on the terminal.

