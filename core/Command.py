# coding:utf-8
import abc
from core.Printer import *
from core.Help import *

command_word = []

class BaseCommand:
    metaclass__ = abc.ABCMeta

    # TODO 自动载入到补全
    help = ''
    word = ''

    def __init__(self):
        command_word.append(self.word)

    @abc.abstractclassmethod
    def run(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

class Exit(BaseCommand):
    word = 'exit'

    def run(self, state,  *args, **kwargs):
        exit(0)

class Help(BaseCommand):
    word = 'help'

    def run(self, state,  *args, **kwargs):
        print_info(global_help)

        if state == 'module':
            print_info(module_help)

class Search(BaseCommand):
    word = 'search'

class CommandInput():
    """
    """

    def __init__(self):
        self.state = 'run'
        self.state_dict = {'run':[]}

    def registered(self,stateList, command: BaseCommand):
        if stateList == 'all':
            stateList = self.state_dict.keys()
        for state in stateList:
            if not state in self.state_dict.keys():
               self.state_dict[state] = []
            self.state_dict[state].append(command)

    def input(self, input: str) -> bool:
        inputList = input.split()
        for command in self.state_dict[self.state]:
            if inputList[0] == command.word:
                command(self.state, inputList)
                return True
        return False

command_handle = CommandInput()
command_handle.registered('all', Exit())
command_handle.registered('all', Help())
