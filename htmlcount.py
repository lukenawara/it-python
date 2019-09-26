import os
from banner import banner
banner("HTML TAG COUNTER", "Luke")

def load(filename):
    data = []
    if os.path.exists(filename):
        print(f"..... loading from {filename}")
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def main():
    run_event_loop()

def run_event_loop():
    filename = input("please enter the name of an HTML file: ")
    data = load(filename)
    tags = 0
    for line in data:
        line_tags = count_tags(line)
        tags = tags + line_tags
    print(f"The file {filename} contains {tags} tags.")


def count_tags(text):
    count = 0
    previous_char = None
    for char in text:
        if char != "/" and previous_char == "<":
            count += 1
        previous_char = char
    return count




main()