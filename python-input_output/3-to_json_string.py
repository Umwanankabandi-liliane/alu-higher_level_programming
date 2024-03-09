#!/usr/bin/python3

def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
