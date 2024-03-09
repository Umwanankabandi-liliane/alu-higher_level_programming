#!usr/bin/python3

"""Defines a text file-reading function."""


def read_lines(filename="", nb_lines=0):
    """Print a given nuber of lines from a UTP8 text fileto stdout.
    Args:
        filenmae (str): The name of the file.
        nb_lines (int): The number of lines to read from the file.
    """
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        lines = 0
        for line in f:
            lines += 1
        f.seek(0)
        if nb_lines >= lines:
            print(f.read(), end="")

        else:
            n = 0
            while n < nb_lines:
                print(f.readlines(), end="")
                n += 1



