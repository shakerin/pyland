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


