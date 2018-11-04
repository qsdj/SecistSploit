#!/usr/bin/env python
# encoding: utf-8
# Copyright 2018, The RouterSploit Framework (RSF) by Threat9 All rights reserved.
import abc
from core.Exploit import BaseExploit
from core.Printer import print_error


class BaseEncoder(BaseExploit):
    metaclass__ = abc.ABCMeta
    architecture = None

    def __init__(self):
        self.module_name = self.__module__.replace("modules.encoders.", "").replace(".", "/")

    @abc.abstractclassmethod
    def encode(self, payload):
        pass

    @staticmethod
    def run():
        print_error("Module cannot be run")

    def __str__(self):
        return self.module_name

    def __format__(self, format_spec):
        return format(self.module_name, format_spec)
