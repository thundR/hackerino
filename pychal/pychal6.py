from zipfile import ZipFile
import re

number = 90052
pattern = re.compile(r".*nothing is (\d+)", re.DOTALL)

seenChars = []
with ZipFile('channel.zip') as zip:
    while True:
        file = str(number) + ".txt"
        with zip.open(file) as f:
            text = f.read().decode('utf-8')
            match = pattern.match(text)
            if match:
                number = match.group(1)
                char = zip.getinfo(file).comment
                if char not in seenChars:
                    seenChars.append(char)
            else:
                print (str(seenChars))
                break