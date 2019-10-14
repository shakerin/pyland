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
    """test name format : test_{className/methodName}_{unit_for_test}"""
    def test_TemlateInfo_original(self):
        """internal variable original value check"""
        ins = TI("ins1", "This is a $frame")
        assert ins.original=="This is a $frame"

    def test_TemlateInfo_key_words(self):
        """internal variable key_word check"""
        ins = TI("ins2", "This is a $frame $string")
        assert listCmp(ins.key_words, ['frame', 'string']) == True
    
    def test_TemlateInfo_Generated_code(self):
        """generated code from the template check"""
        ins = TI("ins3","I am $name, Who are $you. $name is me.")
        generated_code = ins.getGeneratedCode([("name", "Haha"), ("you", "None")])
        assert generated_code == "I am Haha, Who are None. Haha is me."

    def test_TemplateInfo_name(self):
        """check if the name of template is stored properly"""
        ins = TI("nightmare","I am $name, Who are $you. $name is me.")
        assert ins.name == "nightmare"

    def test_TemplateInfo_names(self):
        """check if the class variable names stores all instance names properly"""
        instances = TI.names + ["nightmare"]
        ins1 = TI("nightmare","I am $name, Who are $you. $name is me.")
        assert listCmp(TI.names,instances) == True

    def test_FileToTemplate_file_path(self):
        """check if the file_path variable is stored properly"""
        filepath = "/mnt/c/work/py-work/tests/test_frame_file_1.txt"
        ins1 = FTT("instance1", filepath)
        assert ins1.file_path == filepath

    def test_FileToTemplate_original(self):
        """internal variable original value check"""
        filepath = "/mnt/c/work/py-work/tests/test_frame_file_1.txt"
        ins = FTT("instance1", filepath)
        frame_string = ""
        with open(filepath, 'r') as f:
            frame_string = f.read()
        assert ins.original==frame_string

    def test_FileToTemplate_key_words(self):
        """internal variable key_words value check"""
        filepath = "/mnt/c/work/py-work/tests/test_frame_file_1.txt"
        ins = FTT("instance1", filepath)
        assert listCmp(ins.key_words,['something', 'mood']) == True

    def test_FileToTemplate_Generated_code(self):
        """check generated code is okay"""
        filepath = "/mnt/c/work/py-work/tests/test_frame_file_1.txt"
        genfilepath = "/mnt/c/work/py-work/tests/test_frame_file_1_gc.txt"
        ins = FTT("instance1", filepath)
        generated_string = ""
        with open(genfilepath, 'r') as f:
            generated_string = f.read()
        generated_code = ins.getGeneratedCode([("something", "smile"), ("mood", "serious")])
        assert generated_code == generated_string

    def test_FileToTemplate_name(self):
        """check if the name variable is stored properly"""
        filepath = "/mnt/c/work/py-work/tests/test_frame_file_1.txt"
        ins1 = FTT("drStrange", filepath)
        assert ins1.name == "drStrange"

    def test_FileToTemplate_names(self):
        """check if the name variable is stored properly"""
        filepath = "/mnt/c/work/py-work/tests/test_frame_file_1.txt"
        instances = TI.names + ["drStrange"]
        ins1 = FTT("drStrange", filepath)
        assert listCmp(TI.names,instances) == True