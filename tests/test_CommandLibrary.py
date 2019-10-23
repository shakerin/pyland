#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from os.path import join

from ucg.TemplateInfo import TemplateInfo as TI
from ucg.FileToTemplate import FileToTemplate as FTT
from ucg.TemplateLibrary import TemplateLibrary as TL
from ucg.CommandLibrary import CommandLibrary as CL

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

class TestCommandLibrary:
    """test name format : test_{className/methodName}_{unit_for_test}"""

    def test_CommandLibrary_loadFrameFilesFromDir_frame_dirs(self):
        """check the internal list frame_dirs after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = CL()
        ins.loadFrameFilesFromDir("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest")
        expected_frame_dirs = []
        assert expected_frame_dirs == ins.frame_dirs

    def test_CommandLibrary_frame_dirs(self):
        """this test checks if the frame_dirs are stored properly or not."""
        ins_22= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        ins_22.addFrameDirs(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        exp_frame_dirs = [
            "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest",
            "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"
        ]
        assert sorted(ins_22.frame_dirs)==sorted(exp_frame_dirs)

    def test_CommandLibrary_frame_dirs_CheckOneDirIsNotAddedTwice(self):
        """this test checks if the frame_dirs are stored properly or not."""
        ins_22= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest", 
                    "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        ins_22.addFrameDirs(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        exp_frame_dirs = [
            "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest",
            "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"
        ]
        assert sorted(ins_22.frame_dirs)==sorted(exp_frame_dirs)

    def test_CommandLibrary_loadFrameFilesFromDir_frame_files(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = CL()
        ins.loadFrameFilesFromDir("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest")
        expected_list = ["test_file_1.txt", "test_file_2.txt", "test_file_3"]
        expected_abspath_list = [join("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest", f) for f in expected_list] 
        assert listCmp(expected_abspath_list, ins.frame_files) == True

    def test_CommandLibrary_loadFrameFilesFromDir_frame_names(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = CL()
        ins.loadFrameFilesFromDir("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest")
        expected_frame_names = ["test_file_1", "test_file_2", "test_file_3"]
        assert listCmp(expected_frame_names, ins.frame_names) == True

    def test_CommandLibrary_loadAllTemplates_frame_files(self):
        """check the internal list frame_files after creating CL object with path"""
        ins = CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest","/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        expected_list = ["test_file_1.txt", "test_file_2.txt", "test_file_3"]
        expected_abspath_list = [join("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest", f) for f in expected_list] 
        expected_list1 = ["test_file_4.txt", "test_file_5.txt", "test_file_6"]
        expected_abspath_list1 = [join("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2", f) for f in expected_list1]         
        final_expected_abspath_list = expected_abspath_list + expected_abspath_list1
        assert listCmp(final_expected_abspath_list, ins.frame_files) == True

    def test_CommandLibrary_loadAllTemplates_frame_names(self):
        """check the internal list frame_name after creating CL object with path"""
        ins_4 = CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest","/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        expected_frame_names = ["test_file_1", "test_file_2", "test_file_3", "test_file_4", "test_file_5", "test_file_6"]
        assert listCmp(expected_frame_names, ins_4.frame_names) == True

    def test_CommandLibrary_loadAllTemplates_DynamicObjectInternalVariable_name(self):
        """test the internal variable 'name' that is stored in frame object
        matches the file name string until file extension"""
        ins_5= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest","/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        assert "test_file_1" == ins_5.test_file_1.name

    def test_CommandLibrary_loadAllTemplates_DynamicObjectsCreated(self):
        """check which frame objects are created from the frame directory"""
        ins_6= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        assert sorted(ins_6.frame_names) == sorted(["test_file_1", "test_file_2", "test_file_3"])

    def test_CommandLibrary_loadAllTemplates_ListOfFrameFiles(self):
        """check the file paths of the created frame objects are correct"""
        ins_8= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        dirpath = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest/"
        filepaths = [
            dirpath + "test_file_1.txt",
            dirpath + "test_file_2.txt",
            dirpath + "test_file_3",
        ]
        assert sorted(ins_8.frame_files)==sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_DynamicObjects_FrameLocationSearch(self):
        """check the method for searching particular frame object is correct"""
        ins_9 = CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest","/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        assert ins_9.findFrame("test_file_6") == "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/test_file_6" 

    def test_CommandLibrary_loadAllTemplates_DynamicObjectInternalVariable_key_words(self):
        """test the internal variable 'key_words' that is stored in frame object
        matches the actual number of keywords in frame file"""
        ins_5= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest","/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"])
        assert sorted(ins_5.test_file_1.key_words) == sorted(["number", "name"])

    def test_CommandLibrary_loadAllTemplates_DynamicObjectsUsage(self):
        """check the generated text from particular frame object is correct"""
        ins_7= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        generated_code = ins_7.test_file_2.getGeneratedCode([('word','FILE'),('check','TEST')])
        assert generated_code == "this is single FILE framefile just to TEST"

    def test_CommandLibrary_loadAllTemplates_addFrameDirs_FalseCheck(self):
        """check number of frames are different when all frame_dirs are not 
        included in the class object"""
        ins_10= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        dirpath = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest/"
        dirpath2 = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/"
        filepaths = [
            dirpath + "test_file_1.txt",
            dirpath + "test_file_2.txt",
            dirpath + "test_file_3",
            dirpath2 + "test_file_4.txt",
            dirpath2 + "test_file_5.txt",
            dirpath2 + "test_file_6",
        ]
        assert sorted(ins_10.frame_files)!=sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_addFrameDirs_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_11= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        ins_11.addFrameDirs(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/"])
        dirpath = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest/"
        dirpath2 = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/"
        filepaths = [
            dirpath + "test_file_1.txt",
            dirpath + "test_file_2.txt",
            dirpath + "test_file_3",
            dirpath2 + "test_file_4.txt",
            dirpath2 + "test_file_5.txt",
            dirpath2 + "test_file_6",
        ]
        assert sorted(ins_11.frame_files)==sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_addFrameFromFile_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_12= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        ins_12.addFrameFromFile("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/test_file_4.txt")
        dirpath = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest/"
        dirpath2 = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/"
        filepaths = [
            dirpath + "test_file_1.txt",
            dirpath + "test_file_2.txt",
            dirpath + "test_file_3",
            dirpath2 + "test_file_4.txt",
        ]
        assert sorted(ins_12.frame_files)==sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_addFrameFromFile_FalseCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_13= CL(["/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"])
        ins_13.addFrameFromFile("/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/test_file_10.txt")
        dirpath = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest/"
        dirpath2 = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2/"
        filepaths = [
            dirpath + "test_file_1.txt",
            dirpath + "test_file_2.txt",
            dirpath + "test_file_3",
        ]
        assert sorted(ins_13.frame_files)==sorted(filepaths)