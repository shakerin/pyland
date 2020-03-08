#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from os.path import join
import os
from ucg.TemplateInfo import TemplateInfo as TI
from ucg.FileToTemplate import FileToTemplate as FTT
from ucg.TemplateLibrary import TemplateLibrary as TL
from ucg.Structure import Structure
from tests.path_variables import *


class TestStructure:

    
    structure_file_path_main = PV_testdir_Structure + "/structure_1.struct"
    structure_main = Structure(structure_file_path_main)
    
    
    def test_Structure_OriginalList(self):
        with open(TestStructure.structure_file_path_main, 'r') as f:
            read_lines = f.readlines()
        read_lines = list(filter(None, read_lines))
        newline_replaced = "____".join(read_lines)
        newline_replaced_2 = re.sub(r'{.*?}', 
                                    lambda x:x.group().replace("\n", "").replace("____", ""), 
                                    newline_replaced, 
                                    flags=re.DOTALL)
        read_lines = newline_replaced_2.split("____")
        assert sorted(TestStructure.structure_main.original_list) == sorted(read_lines)



    def test_Structure_Filenames(self):
        assert sorted(TestStructure.structure_main.file_names) == sorted([
                                                                        "file1.txt",
                                                                        "file2.txt",
                                                                        "file3.txt",
                                                                        "file1.txt",
                                                                        "file2.txt",
                                                                        "file3.txt",
                                                                        ])

    def test_Structure_Dirnames(self):
        assert sorted(TestStructure.structure_main.dir_names) ==  sorted([
                                                                        "to_be_deleted_test1",
                                                                        "test2",
                                                                        "test4",
                                                                        "test5",
                                                                        "to_be_deleted_test3",
                                                                        "to_be_deleted_test88",
                                                                        ])

    def test_Structure_FileNDirnames(self):
        assert sorted(TestStructure.structure_main.file_n_dir_names) ==  sorted([
                                                                                "to_be_deleted_test1",
                                                                                "test2",
                                                                                "test4",
                                                                                "test5",
                                                                                "to_be_deleted_test3",
                                                                                "to_be_deleted_test88",
                                                                                "file1.txt",
                                                                                "file2.txt",
                                                                                "file3.txt",
                                                                                "file1.txt",
                                                                                "file2.txt",
                                                                                "file3.txt",
                                                                                ])

    def test_Structure_CMDnames(self):
        assert (TestStructure.structure_main.cmd_names) ==  ([
                                                                "abc",
                                                                "frameObj{}",
                                                                "newObj()",
                                                                "newObj()",
                                                                "",
                                                                "newObj()",
                                                                "newObj()",
                                                                "newObj()",
                                                                "",
                                                                "",
                                                                "",
                                                                "",
                                                                ])


    def test_Structure_positions_dir_only(self):
        assert TestStructure.structure_main.positions_dir_only == [
                                                                        0,
                                                                            4,
                                                                                8,
                                                                            4,
                                                                        0,
                                                                        0,
                                                                        ]


    def test_Structure_positions_dir_only(self):
        assert TestStructure.structure_main.positions == [
                                                                            0,
                                                                                4,
                                                                                4,
                                                                                4,
                                                                                4,
                                                                                    8,
                                                                                    8,
                                                                                    8,
                                                                                    8,
                                                                                4,
                                                                            0,
                                                                            0,
                                                                            ]

    def test_Structure_cmd_types(self):
        assert TestStructure.structure_main.cmd_types == [
                                                                            "DIR",
                                                                                "FILE",
                                                                                "FILE",
                                                                                "FILE",
                                                                                "DIR",
                                                                                    "FILE",
                                                                                    "FILE",
                                                                                    "FILE",
                                                                                    "DIR",
                                                                                "DIR",
                                                                            "DIR",
                                                                            "DIR",
                                                                            ]



    def test_Structure_directoryPaths(self):
        assert (TestStructure.structure_main.dir_paths) == ( \
                                                        [
                                                        'to_be_deleted_test1/',
                                                        'to_be_deleted_test1/test2/',
                                                        'to_be_deleted_test1/test2/test4/',
                                                        'to_be_deleted_test1/test5/',
                                                        'to_be_deleted_test3/',
                                                        'to_be_deleted_test88/'])
    
    def test_Structure_FilePaths(self):
        assert (TestStructure.structure_main.file_paths) == ( \
                                                        [
                                                        'to_be_deleted_test1/file1.txt',
                                                        'to_be_deleted_test1/file2.txt',
                                                        'to_be_deleted_test1/file3.txt',
                                                        'to_be_deleted_test1/test2/file1.txt',
                                                        'to_be_deleted_test1/test2/file2.txt',
                                                        'to_be_deleted_test1/test2/file3.txt'
                                                        ])

    def test_Structure_Commands(self):
        assert (TestStructure.structure_main.commands) == ( \
                                                        [
                                                        ('DIR', 'to_be_deleted_test1/', 'abc'),
                                                        ('DIR', 'to_be_deleted_test1/test2/', ''),
                                                        ('DIR', 'to_be_deleted_test1/test2/test4/', ''),
                                                        ('DIR', 'to_be_deleted_test1/test5/', ''),
                                                        ('DIR', 'to_be_deleted_test3/', ''),
                                                        ('DIR', 'to_be_deleted_test88/', ''),
                                                        ('FILE', 'to_be_deleted_test1/file1.txt', 'frameObj{}'),
                                                        ('FILE', 'to_be_deleted_test1/file2.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/file3.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/test2/file1.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/test2/file2.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/test2/file3.txt', 'newObj()'),
                                                        ])
 



