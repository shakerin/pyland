#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from ucg.TemplateInfo import TemplateInfo as TI
from ucg.FileToTemplate import FileToTemplate as FTT

def listCmp(list1, list2):
    match = True
    if len(list1) == len(list2):
        for i in list1:
            if i in list2:
                pass
            else:
                match = False
                break
    else:
        match = False
    return match

class TestTop:
    def test_TemlateInfo_original(self):
        """internal variable original value check"""
        ins = TI("This is a $frame")
        assert ins.original=="This is a $frame"

    def test_TemlateInfo_key_words(self):
        """internal variable original value check"""
        ins = TI("This is a $frame $string")
        assert listCmp(ins.key_words, ['frame', 'string']) == True
    
    def test_TemlateInfo_Generated_code(self):
        """internal variable original value check"""
        ins = TI("I am $name, Who are $you. $name is me.")
        generated_code = ins.getGeneratedCode([("name", "Haha"), ("you", "None")])
        assert generated_code == "I am Haha, Who are None. Haha is me."
