#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from os.path import join

from ucg.TemplateInfo import TemplateInfo as TI
from ucg.FileToTemplate import FileToTemplate as FTT
from ucg.TemplateLibrary import TemplateLibrary as TL

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

class TestTemplateLibrary:
    """test name format : test_{className/methodName}_{unit_for_test}"""
    def test_TemplateLibrary_loadFrameFilesFromDir_frame_files(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = TL()
        ins.loadFrameFilesFromDir("/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest")
        expected_list = ["test_file_1.txt", "test_file_2.txt", "test_file_3"]
        expected_abspath_list = [join("/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest", f) for f in expected_list] 
        assert listCmp(expected_abspath_list, ins.frame_files) == True

    def test_TemplateLibrary_loadFrameFilesFromDir_frame_names(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = TL()
        ins.loadFrameFilesFromDir("/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest")
        expected_frame_names = ["test_file_1", "test_file_2", "test_file_3"]
        assert listCmp(expected_frame_names, ins.frame_names) == True

    def test_TemplateLibrary_loadAllTemplates_frame_files(self):
        """check the internal list frame_files after creating TL object with path"""
        ins = TL(["/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest","/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest2"])
        expected_list = ["test_file_1.txt", "test_file_2.txt", "test_file_3"]
        expected_abspath_list = [join("/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest", f) for f in expected_list] 
        expected_list1 = ["test_file_4.txt", "test_file_5.txt", "test_file_6"]
        expected_abspath_list1 = [join("/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest2", f) for f in expected_list1]         
        final_expected_abspath_list = expected_abspath_list + expected_abspath_list1
        assert listCmp(final_expected_abspath_list, ins.frame_files) == True

    def test_TemplateLibrary_loadAllTemplates_frame_names(self):
        """check the internal list frame_name after creating TL object with path"""
        ins = TL(["/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest","/mnt/c/work/py-work/tests/testdir_TemplateLibraryTest2"])
        expected_frame_names = ["test_file_1", "test_file_2", "test_file_3", "test_file_4", "test_file_5", "test_file_6"]
        assert listCmp(expected_frame_names, ins.frame_names) == True

