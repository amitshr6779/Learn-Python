import random
from webbrowser import get
def get_file_extension(filename):
    return filename[filename.index(".") + 1:]

def throw_dice(num):
    return random.randint(1, num)