#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from .context import *
from .path_variables import *


class TestFileToTemplate:

    def test_FileToTemplate_file_path(self):
        """check if the file_path variable is stored properly"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        ins1 = FTT("instance1", filepath)
        assert ins1.file_path == filepath

    def test_FileToTemplate_original(self):
        """internal variable original value check"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        ins = FTT("instance1", filepath)
        frame_string = ""
        with open(filepath, 'r') as f:
            frame_string = f.read()
        assert ins.original==frame_string

    def test_FileToTemplate_key_words(self):
        """internal variable key_words value check"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        ins = FTT("instance1", filepath)
        assert sorted(ins.key_words) == sorted(['something', 'mood'])

    def test_FileToTemplate_Generated_code(self):
        """check generated code is okay"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        genfilepath = PV_testdir_FilesToTemplate_FrameFilesOutput + "/test_frame_file_1.txt"
        ins = FTT("instance1", filepath)
        generated_string = ""
        with open(genfilepath, 'r') as f:
            generated_string = f.read()
        generated_code = ins.getGeneratedCode({
                                                "something" : "smile", 
                                                "mood":"serious"
                                              })
        assert generated_code == generated_string

    def test_FileToTemplate_name(self):
        """check if the name variable is stored properly"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        ins1 = FTT("drStrange", filepath)
        assert ins1.name == "drStrange"

    def test_FileToTemplate_Generated_code_DefaultValueOfKeyWords(self):
        """check generated code is okay when argument is missing for frames"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        genfilepath = PV_testdir_FilesToTemplate_FrameFilesOutput + "/test_frame_file_1.txt"
        ins2 = FTT("instance1", filepath)
        generated_string = ""
        with open(genfilepath, 'r') as f:
            generated_string = f.read()
        generated_code = ins2.getGeneratedCode({
                                                "something" : "smile"
                                              })
        generated_string = generated_string.replace("serious", "")
        assert generated_code == generated_string

    def test_FileToTemplate_Generated_code_DefaultValueOfExtraKeyWordsAndMissingKeyword(self):
        """check generated code is okay when extra inputs provided for frame object"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        genfilepath = PV_testdir_FilesToTemplate_FrameFilesOutput + "/test_frame_file_1.txt"
        ins2 = FTT("instance1", filepath)
        generated_string = ""
        with open(genfilepath, 'r') as f:
            generated_string = f.read()
        generated_code = ins2.getGeneratedCode({
                                                "something" : "smile",
                                                "nothing" : "lol"
                                              })
        generated_string = generated_string.replace("serious", "")
        assert generated_code == generated_string

    def test_FileToTemplate_Generated_code_DefaultValueOfExtraKeyWords(self):
        """check generated code is okay when extra inputs provided for frame object"""
        filepath = PV_testdir_FilesToTemplate_FrameFiles + "/test_frame_file_1.txt"
        genfilepath = PV_testdir_FilesToTemplate_FrameFilesOutput + "/test_frame_file_1.txt"
        ins2 = FTT("instance1", filepath)
        generated_string = ""
        with open(genfilepath, 'r') as f:
            generated_string = f.read()
        generated_code = ins2.getGeneratedCode({
                                                "something" : "smile",
                                                "nothing" : "lol",
                                                "mood":"serious"
                                              })
        assert generated_code == generated_string




