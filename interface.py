#!/usr/bin/env python3

import sys
from expert import *
from valid import valid_syntax


def list_to_string(stuff):
    if len(stuff) == 1:
        fmt = "{}"
    elif len(stuff) == 2:
        fmt = "{} and {}"
    else:
        fmt = "{}, " * (len(stuff) - 1) + "and {}"
    return fmt.format(*stuff)


def main():
    if len(sys.argv) == 1:
        print("Gimme file, I need file")
        exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            if valid_syntax(file):
                facts = FactCollection.from_file(file)
            else:
                exit()
        for q in facts.queries:
            facts.facts[q].status = facts.truth_check(q)
            print(q, "is", facts.facts[q].status)
    except OSError:
        print("Gimme valid file, I need file")


if __name__ == "__main__":
    main()
