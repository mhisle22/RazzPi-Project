#!/usr/bin/python
import cgi
import os
import time


print "Content-type: text/html\n"
print "<HTML><HEAD>"
print '<meta http-equiv="refresh" content="3">'
print "</HEAD><BODY>"



print "<h2>Choose an option with the remote.</h2>"
print "<TABLE BORDER='7'><TR><TD><u>Action</u></TD><TD><u>Button #</u></TD></TR>"

print '<TR><TD>Say hi!</TD><TD>1</TD></TR>'
print '<TR><TD>Handshake.</TD><TD>2</TD></TR>'
print '<TR><TD>Button.</TD><TD>3</TD></TR>'
print '<TR><TD>Tilt.</TD><TD>4</TD></TR>'
print '<TR><TD>How far away are you?</TD><TD>5</TD></TR>'
print '<TR><TD>Play a song!</TD><TD>6</TD></TR>'
print '<TR><TD>Calculator.</TD><TD>7</TD></TR>'
print '<TR><TD>Take a picture.</TD><TD>8</TD></TR>'
print '<TR><TD>Record a video.</TD><TD>9</TD></TR>'
print "</TABLE>"

filename = open("/usr/lib/cgi-bin/display.txt","r")
display1 = filename.readline()
display2 = filename.readline()
if display1 == 'camera\n':
    display3 = filename.readline()
    print '<h3>' + display2 + '<br>' + display3 + '</h3>'
    print '<br><br>'
    print '<img src=/image.gif alt="Waiting for a picutre..." width="300" height="300">'
elif display1 == "video\n":
    display3 = filename.readline()
    print '<h3>' + display2 + '<br>' + display3 + '</h3>'
    print '<br><br>'
    #print '<video src="/video.h264" alt="Video" width="400" height="400" autoplay></video>'
else:
    print '<h3>' + display1 + '<br>' + display2 + '</h3>'

filename.close()

print "</BODY></HTML>"








