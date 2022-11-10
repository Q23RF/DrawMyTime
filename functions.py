from PIL import Image
import random
from os import listdir
from os.path import isfile, join

def all_fn(dir):
    return [f for f in listdir('albums/'+dir) if isfile(join('albums/'+dir, f))]

def draw_card(cards, dir):
    d = random.randint(0, len(cards) - 1)
    return 'albums/' + dir + '/' + cards[d]