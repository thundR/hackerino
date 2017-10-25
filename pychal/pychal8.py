import bz2
import re
from urllib.request import urlopen
import codecs

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
response = urlopen(url).read().decode('unicode_escape')
patternUn = re.compile(r"un: '(.+)'")
patternPw = re.compile(r"pw: '(.+)'")
unStr = patternUn.search(response).group(1)
pwStr = patternPw.search(response).group(1)


unZip = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pwZip = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

un = bz2.decompress(bytearray(unStr, "latin1"))
pw = bz2.decompress(bytearray(pwStr, "latin1"))
print("uw: " + un.decode('utf-8'))
print("pw: " + pw.decode('utf-8'))
