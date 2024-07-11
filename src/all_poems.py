import json
from get_poems import get_all_poems


def main():
    with open("texts/poets.txt") as poets:
        poets = poets.read().splitlines()
    print(poets)
    poets = [poet.split(" ") for poet in poets]
    poems = []
    for poet in poets:
        filename = "texts/" + poet[1] + ".txt"
        print(f"Retrieving {filename}")
        first_name, last_name = poet[0], poet[1]
        list_of_poems = get_all_poems(filename, first_name, last_name)
        poems.append(list_of_poems)
    poems = [poem for list_of_poems in poems for poem in list_of_poems]
    for ix, poem in enumerate(poems):
        poem["id"] = ix
    poems_to_dict = {"poems": poems}
    print(len(poems_to_dict["poems"]))
    target_file = "out/poems.json"
    with open(target_file, "w") as poems_file:
        json.dump(poems_to_dict, poems_file)


if __name__ == "__main__":
    main()
