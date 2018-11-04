#!/usr/bin/env python
# encoding: utf-8
# Copyright 2018, The RouterSploit Framework (RSF) by Threat9 All rights reserved.
import logging.handlers
import sys
from core.Printer import print_error
from core.Main import Interpreter
if sys.version_info.major < 3:
    print_error("SecistSploit support only Python 3, Re-run SecistSploit at Python3 environment")
    exit(0)
<<<<<<< HEAD
=======
log_handler = logging.handlers.RotatingFileHandler(filename="secistsploit_attack.log", maxBytes=500000)
log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s       %(message)s")
log_handler.setFormatter(log_formatter)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(log_handler)

>>>>>>> 4902023754ed2bd51b05f9ab9f223165855f24d7

def framework():
    """ Start SecistSploit framework """
    framework_instance = Interpreter()
    framework_instance.run()


if __name__ == '__main__':
    framework()
