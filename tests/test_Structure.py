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
    
    def test_Structure_directoryPaths(self):
        structure_file_path = PV_testdir_Structure + "/structure_1.struct"
        structure_1 = Structure(structure_file_path, PV_testdir_Frames)
        assert sorted(structure_1.abs_paths) == sorted( \
                                                        [
                                                        'to_be_deleted_test1/',
                                                        'to_be_deleted_test1/test2/',
                                                        'to_be_deleted_test1/test2/test4/',
                                                        'to_be_deleted_test1/test5/',
                                                        'to_be_deleted_test3/',
                                                        'to_be_deleted_test88/'])
    
    def test_Structure_FilePaths(self):
        structure_file_path = PV_testdir_Structure + "/structure_1.struct"
        structure_1 = Structure(structure_file_path, PV_testdir_Frames)
        assert sorted(structure_1.abs_filepaths) == sorted( \
                                                        [
                                                        'to_be_deleted_test1/file1.txt',
                                                        'to_be_deleted_test1/file2.txt',
                                                        'to_be_deleted_test1/file3.txt',
                                                        'to_be_deleted_test1/test2/file1.txt',
                                                        'to_be_deleted_test1/test2/file2.txt',
                                                        'to_be_deleted_test1/test2/file3.txt'
                                                        ])
    

    def test_Structure_DirCreation_Check(self):
        structure_file_path = PV_testdir_Structure + "/structure_1.struct"
        structure_1 = Structure(structure_file_path, PV_testdir_Frames)
        root_dirs = ["to_be_deleted_test1", "to_be_deleted_test3", "to_be_deleted_test88"]
        created_dirs = ["to_be_deleted_test1/", "to_be_deleted_test3/", "to_be_deleted_test88/"]
        for root_dir in root_dirs:
            for root, dirs, files in os.walk(root_dir):
                if len(dirs)>0:
                    for dir_name in dirs:
                        dirpath = os.path.join(root, dir_name) + "/"
                        created_dirs.append(dirpath)
        print (structure_1.abs_paths)
        print(created_dirs)
        assert sorted(structure_1.abs_paths) == sorted(created_dirs)

    def test_Structure_FileCreation_Check(self):
        structure_file_path = PV_testdir_Structure + "/structure_1.struct"
        structure_1 = Structure(structure_file_path, PV_testdir_Frames)
        root_dirs = ["to_be_deleted_test1", "to_be_deleted_test3", "to_be_deleted_test88"]
        created_files = []
        for root_dir in root_dirs:
            for root, dirs, files in os.walk(root_dir):
                if len(files)>0:
                    for file_name in files:
                        filepath = os.path.join(root, file_name)
                        created_files.append(filepath)
        print (structure_1.abs_filepaths)
        print(created_files)
        assert sorted(structure_1.abs_filepaths) == sorted(created_files)



