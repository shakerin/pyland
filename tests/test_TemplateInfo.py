#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re

from .context import *
from .path_variables import *


class TestTemplateInfo:
    """test name format : test_{className/methodName}_{unit_for_test}"""
    def test_TemlateInfo_original(self):
        """internal variable original value check"""
        ins = TI("ins1", "This is a $frame")
        assert ins.original=="This is a $frame"

    def test_TemlateInfo_key_words(self):
        """internal variable key_word check"""
        ins = TI("ins2", "This is a $frame $string")
        assert sorted(ins.key_words) == sorted(['frame', 'string'])

    def test_TemlateInfo_block_identifier_default(self):
        """internal variable block_identifier default value check"""
        ins = TI("ins2", "This is a $frame $string")
        assert ins.block_identifier == ("<<<", ">>>")

    def test_TemlateInfo_block_identifier_custom(self):
        """internal variable block_identifier custom value check"""
        ins = TI("ins2", "This is a $frame $string", block_identifier=("<___", "___>"))
        assert ins.block_identifier == ("<___", "___>")

    def test_TemlateInfo_block_identifier_custom_start_end_same(self):
        """internal variable block_identifier custom value check when
        start and end search terms are equal"""
        ins = TI("ins2", "This is a $frame $string", block_identifier=("<___", "<___"))
        assert ins.block_identifier == ("<<<", ">>>")

    def test_TemlateInfo_exec_sections_noExecPresentInFrameString(self):
        """internal variable exec_sections check"""
        ins = TI("ins2", "This is a $frame $string")
        assert ins.exec_sections == []

    def test_TemlateInfo_exec_sections_oneExecPresentInFrameString(self):
        """internal variable exec_sections check when one executable string present
        in string"""
        frame_string = "This is a $frame $string\n <<<\n this is a cmd line \n line 2 \n >>>"
        ins = TI("ins2", frame_string)
        assert sorted(ins.exec_sections) == sorted([" this is a cmd line \n line 2 \n"])

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n this is a cmd line \n"
                        " line 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this is a cmd line \n line 4 \n >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = [
                        " this is a cmd line \n line 2 \n", " this is a cmd line \n line 4 \n"
                      ]
        assert sorted(ins.exec_sections) == sorted(output_list)
 

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_customStartEnd(self):
        """internal variable exec_sections check when multiple executable string present
        in string, custom start...end terms provided"""
        frame_string = (
                        "This is a $frame $string\n"
                        " #start\n"
                        " this is a cmd line \n"
                        " line 2 \n"
                        " #end\n"
                        " this is it \n"
                        "#start\n"
                        " this is a cmd line \n"
                        " line 4 \n"
                        " #end"
                        )
        ins = TI("ins2", frame_string, block_identifier=("#start", "#end"))
        output_list = [
                        " this is a cmd line \n line 2 \n", 
                        " this is a cmd line \n line 4 \n"
                      ]
        assert sorted(ins.exec_sections) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_customStartEnd_endmissing(self):
        """internal variable exec_sections check when multiple executable string present
        in string, custom start...end terms provided, end term missing"""
        frame_string = (
                        "This is a $frame $string\n"
                        " #start\n"
                        " this is a cmd line \n"
                        " line 2 \n"
                        " \n"
                        " this is it \n"
                        "#start\n"
                        " this is a cmd line \n"
                        " line 4 \n"
                        " #end"
                        )
        ins = TI("ins2", frame_string, block_identifier=("#start", "#end"))
        output_str = (
                        " this is a cmd line \n"
                        " line 2 \n"
                        " \n"
                        " this is it \n"
                        "#start\n"
                        " this is a cmd line \n"
                        " line 4 \n"
                     )
        output_list = [output_str]
        assert sorted(ins.exec_sections) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_customStartEnd_startmissing(self):
        """internal variable exec_sections check when multiple executable string present
        in string, custom start...end terms provided, start term missing"""
        frame_string = (
                        "This is a $frame $string\n"
                        " \n"
                        " this is a cmd line \n"
                        " line 2 \n"
                        " #end\n"
                        " this is it \n"
                        "#start\n"
                        " this is a cmd line \n"
                        " line 4 \n"
                        " #end"
                        )
        ins = TI("ins2", frame_string, block_identifier=("#start", "#end"))
        assert sorted(ins.exec_sections) == sorted([" this is a cmd line \n line 4 \n"])



    def test_TemlateInfo_Generated_code(self):
        """generated code from the template check"""
        ins = TI("ins3","I am $name, Who are $you. $name is me.")
        generated_code = ins.getGeneratedCode({
                                                "name" : "Haha", 
                                                "you" : "None"
                                              })
        assert generated_code == "I am Haha, Who are None. Haha is me."

    def test_TemplateInfo_name(self):
        """check if the name of template is stored properly"""
        ins = TI("nightmare","I am $name, Who are $you. $name is me.")
        assert ins.name == "nightmare"



    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_ExecLocalVar1(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n this is a __local__cmd1 line \n"
                        " __local__cmd1 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this is a __global__cmd2 line \n line 4 \n >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = ["cmd1"]
        assert sorted(ins.exec_var_local) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_ExecLocalVar2(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n this is a __local__cmd1 line \n"
                        " __local__cmd2 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this is a __global__cmd2 line \n line 4 \n >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = ["cmd1"]
        assert sorted(ins.exec_var_local) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_ExecLocalVar3(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n this is a __local__cmd1 line \n"
                        " __local__cmd2 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this is a __var__cmd2 line \n line 4 \n >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = ["cmd1", "cmd2"]
        assert sorted(ins.exec_var_local) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_ExecGlobalVar1(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n this is a __var__cmd1 line \n"
                        " __global__cmd2 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this is a __var__cmd2 line \n line 4 \n >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = ["cmd2"]
        assert sorted(ins.exec_var_global) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_PythonifyCheck(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n "
                        "__global__this is a cmd line \n"
                        " __local__line 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this __var__is a cmd __global__line \n"
                        " line 4 \n"
                        " >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = [
                        " self.this is a cmd line \n self.line 2 \n", 
                        " this __var__is a cmd self.line \n line 4 \n"
                      ]
        assert sorted(ins.exec_sections) == sorted(output_list)

    def test_TemlateInfo_exec_sections_multipleExecPresentInFrameString_PrintVarsCheck(self):
        """internal variable exec_sections check when multiple executable string present
        in string"""
        frame_string = (
                        "This is a $frame $string\n" 
                        "<<<\n "
                        "__global__this is a cmd line \n"
                        " __local__line 2 \n"
                        " >>>\n"
                        " this is it \n"
                        "<<<\n"
                        " this __var__is a cmd __global__line \n"
                        " __print__==__global__line \n"
                        " >>>"
                        )
        ins = TI("ins2", frame_string)
        output_list = [
                        " self.this is a cmd line \n self.line 2 \n", 
                        " this __var__is a cmd self.line \n self.txt += str(self.line) \n"
                      ]
        assert sorted(ins.exec_sections) == sorted(output_list)


