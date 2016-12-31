import base64
b64 = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
cipher = base64.standard_b64decode(b64).decode("ASCII")
clear = '{"showpassword":"no","bgcolor":"#ffffff"}';
tmpChar = ''
correctVal = 0;
iter = 1
key = ""
fixedb64 = []

for x in range(len(clear)):
    while True:
        if (ord(cipher[x]) ^ iter) == ord(clear[x]):
            key = key + str(chr(iter))
            iter = 1 
            break
        else:
            iter+=1
print(key)

