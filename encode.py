import base64
clear = '{"showpassword":"yes","bgcolor":"#ffffff"}'
key = "qw8J"
cipher = ""

for x in range(len(clear)):
    cipher = cipher + chr(ord(clear[x]) ^ ord(key[x % len(key)]))

print(base64.b64encode(bytes(cipher.encode('ascii'))))


