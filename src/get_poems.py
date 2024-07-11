""" Given a file returns a list of poems in JSON format.
Usage: python3 parse_poems.py first_name last_name filename

Returns:
    List: A list of poems in dict form with keys\
    {title, text, author: first_name, last_name}
"""
import json
import os
from typing import List

NestedList = List[List[str]]


def file_to_data(filename: str) -> tuple[str, str]:
    """Opens a file containing a name and poems.
        Returns a tuple (name, poems)"""
    with open(filename) as raw_poems:
        data = raw_poems.read()
    return data[0], data[1:]


def data_to_poems(data: str, sep: str) -> NestedList:
    """data_to_poems Given a string on multiple poems separated by sep,\
    returns a list of poems, with blank lines removed.

    Args:
        data (str): The poems as one string
        sep (str): A string such as "***"

    Returns:
        NestedList: A list of list
    """
    poems = data.split(sep)
    split_poems = [poem.split("\n") for poem in poems]
    clean_poems = [[verse for verse in poem if verse != ""] for poem
                   in split_poems]
    return clean_poems


def parse_all_poems(poems: NestedList) -> list[dict]:
    """parse_all_poems Given a list of poems returns a list of dictionaries

    Args:
        poems (list[str]): expects a list of lists. First item of each list\
        should be title, rest is poem

    Returns:
        list[dict]: returns a list of poems in the form \
            {"title": title, "text": text of poem}
    """
    titles = [poem[0] for poem in poems]
    texts = [poem[1:] for poem in poems]
    parsed_poems = [
        {"title": title, "text": text} for title, text in zip(titles, texts)
    ]
    return parsed_poems


def add_author(first_name: str, last_name: str, poem: dict):
    """Adds author field to poems"""
    poem["first_name"] = first_name
    poem["last_name"] = last_name
    return poem


def add_author_to_all_poems(first_name, last_name, poems):
    """Adds author to all poems in list. Poems must be in dict format"""
    poems = list(map(lambda poem: add_author(first_name, last_name, poem),
                     poems))
    return poems


def get_all_poems(filename):
    """all_poems Given a filename,
        return a list of poems in dict format.

    Args:
        filename (string): the file to process. The file must contain\
        poems separated by "***".

    Returns:
       poems (List(dict)): a list of poems in dict format
    """
    name, data = file_to_data(filename)
    poems = data_to_poems(data, sep="***")
    poems = parse_all_poems(poems)
    first_name, last_name = name.split(", ")
    poems = add_author_to_all_poems(first_name, last_name, poems)

    return poems


def get_all_poems_from_files(dirpath: str) -> list[dict]:
    """Returns a list of dicts for consumption by main"""
    poems = [get_all_poems(filename) for filename in os.listdir(dirpath)]
    return poems


def main():
    """Navigates directory and writes json to out
    """
    poems = get_all_poems_from_files("texts")
    for idx, poem in enumerate(poems):
        poem["id"] = idx
    poems_to_dict = {"poems": poems}
    print(len(poems_to_dict["poems"]))
    target_file = "out/poems.json"
    with open(target_file, "w") as poems_file:
        json.dump(poems_to_dict, poems_file)


if __name__ == "__main__":
    main()
