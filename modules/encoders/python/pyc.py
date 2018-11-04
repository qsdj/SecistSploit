#!/usr/bin/env python
# encoding: utf-8
import importlib
from core.Encoders import BaseEncoder
from core.Payloads import architectures_wrapper


class Encoder(BaseEncoder):
    __info__ = {
        "name": "python pyc Encoder",
        "description": "Module encodes Python payload to pyc format.",
        "authors": (
            "blue-bird"
        ),
    }
    architecture = architectures_wrapper.PYTHON

    def encode(self, payload):
        source = bytes(payload)
        source_hash = importlib.util.source_hash(source)
        bytecode = importlib._bootstrap_external._code_to_hash_pyc(source, source_hash)
        return str(bytecode)
