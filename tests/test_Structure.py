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
    structure_main = Structure(structure_file_path_main, PV_testdir_Frames)
    
    
    def test_Structure_OriginalList(self):
        with open(TestStructure.structure_file_path_main, 'r') as f:
            read_lines = f.readlines()
        read_lines = list(filter(None, read_lines))
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
                                                                "frameObj()",
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




    def test_Structure_directoryPaths(self):
        assert (TestStructure.structure_main.abs_paths) == ( \
                                                        [
                                                        'to_be_deleted_test1/',
                                                        'to_be_deleted_test1/test2/',
                                                        'to_be_deleted_test1/test2/test4/',
                                                        'to_be_deleted_test1/test5/',
                                                        'to_be_deleted_test3/',
                                                        'to_be_deleted_test88/'])
    
    def test_Structure_FilePaths(self):
        assert (TestStructure.structure_main.abs_filepaths) == ( \
                                                        [
                                                        'to_be_deleted_test1/file1.txt',
                                                        'to_be_deleted_test1/file2.txt',
                                                        'to_be_deleted_test1/file3.txt',
                                                        'to_be_deleted_test1/test2/file1.txt',
                                                        'to_be_deleted_test1/test2/file2.txt',
                                                        'to_be_deleted_test1/test2/file3.txt'
                                                        ])
    
    
    def test_Structure_DirCreation_Check(self):
        root_dirs = ["to_be_deleted_test1", "to_be_deleted_test3", "to_be_deleted_test88"]
        created_dirs = ["to_be_deleted_test1/", "to_be_deleted_test3/", "to_be_deleted_test88/"]
        for root_dir in root_dirs:
            for root, dirs, files in os.walk(root_dir):
                if len(dirs)>0:
                    for dir_name in dirs:
                        dirpath = os.path.join(root, dir_name) + "/"
                        created_dirs.append(dirpath)
        assert sorted(TestStructure.structure_main.abs_paths) == sorted(created_dirs)
    
    def test_Structure_FileCreation_Check(self):
        root_dirs = ["to_be_deleted_test1", "to_be_deleted_test3", "to_be_deleted_test88"]
        created_files = []
        for root_dir in root_dirs:
            for root, dirs, files in os.walk(root_dir):
                if len(files)>0:
                    for file_name in files:
                        filepath = os.path.join(root, file_name)
                        created_files.append(filepath)
        assert sorted(TestStructure.structure_main.abs_filepaths) == sorted(created_files)
    


