import json
import os
with open("texts/poets.txt") as f:
    poets = f.readlines()
with open("out/poems.json", "r") as f:
    poems = json.loads(f.read())["poems"]

names = set([{p["last_name"].capitalize(): p["first_name"].capitalize()}
            for p in poems])

for filename in os.listdir("texts"):
    first, last = filename.split(", ").strip()
    with open(filename, "w") as f:
        line = 
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
