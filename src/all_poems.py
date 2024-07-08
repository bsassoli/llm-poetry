import json
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
for ix, poem in enumerate(poems):
    poem["id"] = ix
poems_to_dict = {"poems": poems}
target_file = "poems.json"
with open(target_file, "w") as poems_file:
    json.dump(poems_to_dict, poems_file)
