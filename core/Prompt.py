# coding:utf-8
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import to_formatted_text, HTML
from core.Command import command_word
from core.Search import *

session = PromptSession()
list_module('modules')

command_completer = WordCompleter(command_word+module_word)

prompt_message = to_formatted_text(HTML('<p fg="blue">>SSF</p> '))
