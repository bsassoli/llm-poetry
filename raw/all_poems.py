import json
from functools import reduce
from parse_poems import all_poems

with open("poets.txt") as poets:
    poets = poets.read().splitlines()

poets = [poet.split(" ") for poet in poets if poet != "giorgio caproni"]
poems = []
for poet in poets:
    filename = poet[1] + ".txt"
    first_name, last_name = poet[0], poet[1]
    list_of_poems = all_poems(filename, first_name, last_name)
    poems.append(list_of_poems)
poems = [poem for list_of_poems in poems for poem in list_of_poems]
poems = json.dumps(poems)
print(poems)
