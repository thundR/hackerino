import re

pattern = re.compile(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")

with open('garbage.txt') as f:
    text = f.read()
    print(pattern.findall(text))