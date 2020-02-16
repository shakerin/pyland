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
from ucg.Pyland import Pyland
from tests.path_variables import *


class TestPyland:

    
    structure_file_path_main = PV_testdir_Structure + "/pyland_main.struct"
    pyland_main = Pyland(structure_file_path_main)
    
    
    def test_Pyland_DirCreation_Check(self):
        root_dirs = ["to_be_deleted_test1", "to_be_deleted_test3", "to_be_deleted_test88"]
        created_dirs = ["to_be_deleted_test1/", "to_be_deleted_test3/", "to_be_deleted_test88/"]
        for root_dir in root_dirs:
            for root, dirs, files in os.walk(root_dir):
                if len(dirs)>0:
                    for dir_name in dirs:
                        dirpath = os.path.join(root, dir_name) + "/"
                        created_dirs.append(dirpath)
        assert sorted(TestPyland.pyland_main.ST1.dir_paths) == sorted(created_dirs)
    
    def test_Pyland_FileCreation_Check(self):
        root_dirs = ["to_be_deleted_test1", "to_be_deleted_test3", "to_be_deleted_test88"]
        created_files = []
        for root_dir in root_dirs:
            for root, dirs, files in os.walk(root_dir):
                if len(files)>0:
                    for file_name in files:
                        filepath = os.path.join(root, file_name)
                        created_files.append(filepath)
        assert sorted(TestPyland.pyland_main.ST1.file_paths) == sorted(created_files)  

    def test_Pyland_OriginalList(self):
        with open(TestPyland.structure_file_path_main, 'r') as f:
            read_lines = f.readlines()
        read_lines = list(filter(None, read_lines))
        assert sorted(TestPyland.pyland_main.ST1.original_list) == sorted(read_lines)




    def test_Pyland_Filenames(self):
        assert sorted(TestPyland.pyland_main.ST1.file_names) == sorted([
                                                                        "file1.txt",
                                                                        "file2.txt",
                                                                        "file3.txt",
                                                                        "file1.txt",
                                                                        "file2.txt",
                                                                        "file3.txt",
                                                                        ])

    def test_Pyland_Dirnames(self):
        assert sorted(TestPyland.pyland_main.ST1.dir_names) ==  sorted([
                                                                        "to_be_deleted_test1",
                                                                        "test2",
                                                                        "test4",
                                                                        "test5",
                                                                        "to_be_deleted_test3",
                                                                        "to_be_deleted_test88",
                                                                        ])

    def test_Pyland_FileNDirnames(self):
        assert sorted(TestPyland.pyland_main.ST1.file_n_dir_names) ==  sorted([
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

    def test_Pyland_CMDnames(self):
        assert (TestPyland.pyland_main.ST1.cmd_names) ==  ([
                                                                "abc",
                                                                "justText{''}",
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


    def test_Pyland_positions_dir_only(self):
        assert TestPyland.pyland_main.ST1.positions_dir_only == [
                                                                        0,
                                                                            4,
                                                                                8,
                                                                            4,
                                                                        0,
                                                                        0,
                                                                        ]


    def test_Pyland_positions_dir_only(self):
        assert TestPyland.pyland_main.ST1.positions == [
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

    def test_Pyland_cmd_types(self):
        assert TestPyland.pyland_main.ST1.cmd_types == [
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



    def test_Pyland_directoryPaths(self):
        assert (TestPyland.pyland_main.ST1.dir_paths) == ( \
                                                        [
                                                        'to_be_deleted_test1/',
                                                        'to_be_deleted_test1/test2/',
                                                        'to_be_deleted_test1/test2/test4/',
                                                        'to_be_deleted_test1/test5/',
                                                        'to_be_deleted_test3/',
                                                        'to_be_deleted_test88/'])
    
    def test_Pyland_FilePaths(self):
        assert (TestPyland.pyland_main.ST1.file_paths) == ( \
                                                        [
                                                        'to_be_deleted_test1/file1.txt',
                                                        'to_be_deleted_test1/file2.txt',
                                                        'to_be_deleted_test1/file3.txt',
                                                        'to_be_deleted_test1/test2/file1.txt',
                                                        'to_be_deleted_test1/test2/file2.txt',
                                                        'to_be_deleted_test1/test2/file3.txt'
                                                        ])

    def test_Pyland_Commands(self):
        assert (TestPyland.pyland_main.ST1.commands) == ( \
                                                        [
                                                        ('DIR', 'to_be_deleted_test1/', 'abc'),
                                                        ('DIR', 'to_be_deleted_test1/test2/', ''),
                                                        ('DIR', 'to_be_deleted_test1/test2/test4/', ''),
                                                        ('DIR', 'to_be_deleted_test1/test5/', ''),
                                                        ('DIR', 'to_be_deleted_test3/', ''),
                                                        ('DIR', 'to_be_deleted_test88/', ''),
                                                        ('FILE', 'to_be_deleted_test1/file1.txt', "justText{''}"),
                                                        ('FILE', 'to_be_deleted_test1/file2.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/file3.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/test2/file1.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/test2/file2.txt', 'newObj()'),
                                                        ('FILE', 'to_be_deleted_test1/test2/file3.txt', 'newObj()'),
                                                        ])

