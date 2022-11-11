import random
from os import listdir
from os.path import isfile, isdir, join

def all_fn(dir,sub):
    return [f for f in listdir('albums/'+dir+'/'+sub) if isfile(join('albums/'+dir+'/'+sub, f))]

def all_dn(dir):
    return [f for f in listdir('albums/'+dir) if isdir(join('albums/'+dir, f))]

def draw_card(cards, dir, sub):
    d = random.randint(0, len(cards) - 1)
    return 'albums/' + dir + '/' +sub +'/' + cards[d]