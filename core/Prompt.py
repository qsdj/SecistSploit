# coding:utf-8
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import to_formatted_text, HTML
from prompt_toolkit.history import FileHistory
from core.Command import command_word
from core.Search import *

history_path = '/tmp/ssfhistory'
if not Path(history_path).exists():
    open(history_path, 'w+').close()
session = PromptSession(history=FileHistory(history_path))
list_module('modules')

command_completer = WordCompleter(command_word+module_word)

prompt_message = to_formatted_text(HTML('<p fg="blue">>SSF</p> '))
