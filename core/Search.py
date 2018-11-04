# coding:utf-8
from os import listdir
from os.path import isfile, join, isdir

module_word = []

module_path = []

def list_module(dir):
    # TODO bug满天飞
    for _ in listdir(dir):
        rel_path = join(dir, _)
        if isdir(rel_path):
            list_module(rel_path)
            module_word.append(_)
        if isfile(rel_path) and _.split('.')[-1] == 'py':
           path = join(dir,_[:-3])
           module_path.append(path)
           module_word.append(path)
