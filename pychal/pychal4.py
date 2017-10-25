import re
from urllib.request import urlopen

pattern = re.compile(r".*and the next nothing is (\d+)", re.DOTALL)
baseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#number = 12345
number= 16044/2

while True:
    url = baseUrl + str(number)
    print(number)
    response = urlopen(url).read().decode('utf-8')
    match = pattern.match(response)
    if match:
        number = match.group(1)
    else:
        print (response)
        break