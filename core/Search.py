# coding:utf-8
from os import listdir
from os.path import isfile, join, isdir

module_word = []

module_path = []

def list_module(dir):
    # TODO bug满天飞
    for _ in listdir(dir):
        module_word.append(_)
        rel_path = join(dir, _)
        if isdir(rel_path):
            list_module(rel_path)

        if isfile(rel_path) and _.split('.')[-1] == 'py':
           module_path.append(join(dir,_[:-3]))
