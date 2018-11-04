#!/usr/bin/env python
# encoding: utf-8
# Copyright 2018, The RouterSploit Framework (RSF) by Threat9 All rights reserved.
import atexit
import itertools
import os
import sys
import traceback
from collections import Counter
from future.builtins import input
from core.Exceptions import StandardException
from core.Utils import *
from core.Printer import *
from core.Exploit import GLOBAL_OPTS
from core.Payloads import BasePayload
from prompt_toolkit import *
from core.Command import command_handle
from core.Prompt import *
from core.Search import *
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
platform = sys.platform


class BaseInterpreter(object):
    def __init__(self):
        self.setup()
        if platform == "linux" or platform == "darwin":
            os.system('clear')
        elif platform == "window":
            os.system('cls')
        self.banner = ""


class Interpreter(BaseInterpreter):
    def __init__(self):
        super(Interpreter, self).__init__()
        PrinterThread().start()
        list_module('modules')

    def run(self):
        while True:
            command = session.prompt(prompt_message, completer=command_completer, complete_while_typing=True, auto_suggest=AutoSuggestFromHistory())
            command_handle.input(command)
