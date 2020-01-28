#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from os.path import join

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
                                                        'test1/',
                                                        'test1/test2/',
                                                        'test1/test2/test4/',
                                                        'test1/test5/',
                                                        'test3/',
                                                        'test88/'])
    """
    def test_Structure_FilePaths(self):
        structure_file_path = PV_testdir_Structure + "/structure_1.struct"
        structure_1 = Structure(structure_file_path, PV_testdir_Frames)
        assert sorted(structure_1.abs_filepaths) == sorted( \
                                                        [
                                                        'test1/file1.txt',
                                                        'test1/file2.txt',
                                                        'test1/file3.txt',
                                                        'test1/test2/file1.txt',
                                                        'test1/test2/file2.txt',
                                                        'test1/test2/file3.txt'
                                                        ])
    """

