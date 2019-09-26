import os


def load(name):
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        print(f"..... loading from {filename}")
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):

    filename = os.path.join(".", "journals" , "f{name}.jrn") # "./journals/default.jrn"
    print(f"..... saving to {filename}")
    with open(filename,'w') as fout:
        for entry in data:
            fout.write(entry+"\n")


def get_full_pathname(name):
   filename = os.path.abspath(os.path.join(".", "journals" , "f{name}.jrn"))
   return filename

def add_entry(text, data):
    data.append(text)
