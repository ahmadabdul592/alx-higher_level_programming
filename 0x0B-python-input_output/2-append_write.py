#!/usr/bin/python3
"""A function that appends a string at the end of text file"""


def append_write(filename="", text=""):
    """appends string to text file
    Args:
        filename: name of file to append to
        text: string to append
    Return: No. of printed chars
    """
    with open(filename, 'a+', encoding="utf8") as f:
        return f.write(text)
