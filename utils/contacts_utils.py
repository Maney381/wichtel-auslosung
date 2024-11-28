import json
import random

# Load the contacs
def load_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except:
        print("Please provide the file in the correct format")

def derange(lst):
    while True:
        shuffled = lst[:]
        random.shuffle(shuffled)
        if all(x != y for x, y in zip(lst, shuffled)):
            return shuffled