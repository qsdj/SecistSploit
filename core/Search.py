# coding:utf-8
from os import listdir
from os.path import isfile, join, isdir

module_word = []

module_path = []

def list_module(dir):
    for _ in listdir(dir):
        module_word.append[_]
        if isdir(_):
            list_module(join(dir, _))
        if isfile(_) and _.split('.')[-1] == 'py':
           module_path.append(join(dir,_[:-3]))
