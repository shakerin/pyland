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


testdir_CommandLibraryTest = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest"
testdir_CommandLibraryTest2 = "/mnt/c/work/py-land/pyland/tests/testdir_CommandLibraryTest2"


class TestCommandLibrary:
    """test name format : test_{className/methodName}_{unit_for_test}"""

    def test_CommandLibrary_loadFrameFilesFromDir_frame_dirs(self):
        """check the internal list frame_dirs after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = CL()
        ins.loadFrameFilesFromDir(testdir_CommandLibraryTest)
        expected_frame_dirs = []
        assert expected_frame_dirs == ins.frame_dirs

    def test_CommandLibrary_frame_dirs(self):
        """this test checks if the frame_dirs are stored properly or not."""
        ins_22= CL([testdir_CommandLibraryTest])
        ins_22.addFrameDirs([testdir_CommandLibraryTest2])
        exp_frame_dirs = [
            testdir_CommandLibraryTest,
            testdir_CommandLibraryTest2
        ]
        assert sorted(ins_22.frame_dirs)==sorted(exp_frame_dirs)

    def test_CommandLibrary_frame_dirs_CheckOneDirIsNotAddedTwice(self):
        """this test checks if the frame_dirs are stored properly or not."""
        ins_22= CL([testdir_CommandLibraryTest, 
                    testdir_CommandLibraryTest2])
        ins_22.addFrameDirs([testdir_CommandLibraryTest2])
        exp_frame_dirs = [
            testdir_CommandLibraryTest,
            testdir_CommandLibraryTest2
        ]
        assert sorted(ins_22.frame_dirs)==sorted(exp_frame_dirs)

    def test_CommandLibrary_loadFrameFilesFromDir_frame_files(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = CL()
        ins.loadFrameFilesFromDir(testdir_CommandLibraryTest)
        expected_list = ["test_file_1.txt", "test_file_2.txt", "test_file_3"]
        expected_abspath_list = [join(testdir_CommandLibraryTest, f) for f in expected_list] 
        assert sorted(expected_abspath_list) == sorted(ins.frame_files)

    def test_CommandLibrary_loadFrameFilesFromDir_frame_names(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = CL()
        ins.loadFrameFilesFromDir(testdir_CommandLibraryTest)
        expected_frame_names = ["test_file_1", "test_file_2", "test_file_3"]
        assert sorted(expected_frame_names) == sorted(ins.frame_names)

    def test_CommandLibrary_loadAllTemplates_frame_files(self):
        """check the internal list frame_files after creating CL object with path"""
        ins = CL([testdir_CommandLibraryTest,testdir_CommandLibraryTest2])
        expected_list = ["test_file_1.txt", "test_file_2.txt", "test_file_3"]
        expected_abspath_list = [join(testdir_CommandLibraryTest, f) for f in expected_list] 
        expected_list1 = ["test_file_4.txt", "test_file_5.txt", "test_file_6"]
        expected_abspath_list1 = [join(testdir_CommandLibraryTest2, f) for f in expected_list1]         
        final_expected_abspath_list = expected_abspath_list + expected_abspath_list1
        assert sorted(final_expected_abspath_list) == sorted(ins.frame_files)

    def test_CommandLibrary_loadAllTemplates_frame_names(self):
        """check the internal list frame_name after creating CL object with path"""
        ins_4 = CL([testdir_CommandLibraryTest,testdir_CommandLibraryTest2])
        expected_frame_names = ["test_file_1", "test_file_2", "test_file_3", "test_file_4", "test_file_5", "test_file_6"]
        assert sorted(expected_frame_names) == sorted(ins_4.frame_names)

    def test_CommandLibrary_loadAllTemplates_DynamicObjectInternalVariable_name(self):
        """test the internal variable 'name' that is stored in frame object
        matches the file name string until file extension"""
        ins_5= CL([testdir_CommandLibraryTest,testdir_CommandLibraryTest2])
        assert "test_file_1" == ins_5.test_file_1.name

    def test_CommandLibrary_loadAllTemplates_DynamicObjectsCreated(self):
        """check which frame objects are created from the frame directory"""
        ins_6= CL([testdir_CommandLibraryTest])
        assert sorted(ins_6.frame_names) == sorted(["test_file_1", "test_file_2", "test_file_3"])

    def test_CommandLibrary_loadAllTemplates_ListOfFrameFiles(self):
        """check the file paths of the created frame objects are correct"""
        ins_8= CL([testdir_CommandLibraryTest])
        dirpath = testdir_CommandLibraryTest
        filepaths = [
            dirpath + "/test_file_1.txt",
            dirpath + "/test_file_2.txt",
            dirpath + "/test_file_3",
        ]
        assert sorted(ins_8.frame_files)==sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_DynamicObjects_FrameLocationSearch(self):
        """check the method for searching particular frame object is correct"""
        ins_9 = CL([testdir_CommandLibraryTest,testdir_CommandLibraryTest2])
        assert ins_9.findFrame("test_file_6") == testdir_CommandLibraryTest2+"/test_file_6" 

    def test_CommandLibrary_loadAllTemplates_DynamicObjectInternalVariable_key_words(self):
        """test the internal variable 'key_words' that is stored in frame object
        matches the actual number of keywords in frame file"""
        ins_5= CL([testdir_CommandLibraryTest,testdir_CommandLibraryTest2])
        assert sorted(ins_5.test_file_1.key_words) == sorted([
                                                              "start", 
                                                              "item", 
                                                              "list_or_dict",
                                                              "do_cmd",
                                                              "end"])

    def test_CommandLibrary_loadAllTemplates_DynamicObjectsUsage(self):
        """check the generated text from particular frame object is correct"""
        ins_7= CL([testdir_CommandLibraryTest])
        generated_code = ins_7.test_file_2.getGeneratedCode({
                                                            'word':'FILE',
                                                            'check':'TEST'
                                                            })
        assert generated_code == "this is single FILE framefile just to TEST"

    def test_CommandLibrary_loadAllTemplates_addFrameDirs_FalseCheck(self):
        """check number of frames are different when all frame_dirs are not 
        included in the class object"""
        ins_10= CL([testdir_CommandLibraryTest])
        dirpath = testdir_CommandLibraryTest
        dirpath2 = testdir_CommandLibraryTest2
        filepaths = [
            dirpath + "/test_file_1.txt",
            dirpath + "/test_file_2.txt",
            dirpath + "/test_file_3",
            dirpath2 + "/test_file_4.txt",
            dirpath2 + "/test_file_5.txt",
            dirpath2 + "/test_file_6",
        ]
        assert sorted(ins_10.frame_files)!=sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_addFrameDirs_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_11= CL([testdir_CommandLibraryTest])
        ins_11.addFrameDirs([testdir_CommandLibraryTest2])
        dirpath = testdir_CommandLibraryTest
        dirpath2 = testdir_CommandLibraryTest2
        filepaths = [
            dirpath + "/test_file_1.txt",
            dirpath + "/test_file_2.txt",
            dirpath + "/test_file_3",
            dirpath2 + "/test_file_4.txt",
            dirpath2 + "/test_file_5.txt",
            dirpath2 + "/test_file_6",
        ]
        assert sorted(ins_11.frame_files)==sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_addFrameFromFile_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_12= CL([testdir_CommandLibraryTest])
        ins_12.addFrameFromFile(testdir_CommandLibraryTest2 + "/test_file_4.txt")
        dirpath = testdir_CommandLibraryTest
        dirpath2 = testdir_CommandLibraryTest2
        filepaths = [
            dirpath + "/test_file_1.txt",
            dirpath + "/test_file_2.txt",
            dirpath + "/test_file_3",
            dirpath2 + "/test_file_4.txt",
        ]
        assert sorted(ins_12.frame_files)==sorted(filepaths)

    def test_CommandLibrary_loadAllTemplates_addFrameFromFile_FalseCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_13= CL([testdir_CommandLibraryTest])
        ins_13.addFrameFromFile(testdir_CommandLibraryTest2 + "/test_file_10.txt")
        dirpath = testdir_CommandLibraryTest
        dirpath2 = testdir_CommandLibraryTest2
        filepaths = [
            dirpath + "/test_file_1.txt",
            dirpath + "/test_file_2.txt",
            dirpath + "/test_file_3",
        ]
        assert sorted(ins_13.frame_files)==sorted(filepaths)


    def test_CommandLibrary_FrameObj_runGeneratedCode_WriteToAFile(self):
        """check if the runGeneratedCode is working fine. In this test, a new file 
        is written with specific value
        
        Command Frame Files : test_file_3 (this is the command executed by 
        runGeneratedCode)
        ------------------------------------------------------------------
        with open("$filepath", "w") as f:
            f.write("$txt")
        ------------------------------------------------------------------
        command frame keywords : filepath, txt
        """
        ins_14 = CL([testdir_CommandLibraryTest])
        txt_2_write = "I am from the class test_CommandLibrary.py"
        ins_14.test_file_3.runGeneratedCode({
                                             'filepath' : testdir_CommandLibraryTest2 + "/test_file_3",
                                             'txt' : txt_2_write
                                             })
        readTxt = ""
        with open(testdir_CommandLibraryTest2+"/test_file_3", "r") as f:
            readTxt = f.read()
        assert readTxt == txt_2_write


    def test_CommandLibrary_FrameObj_runGeneratedCode_ForLoop(self):
        """check if the runGeneratedCode is working fine. In this test, just 
        checking if for loop works
        
        Command Frame Files : test_file_1 (this is the command executed by 
        runGeneratedCode)
        ------------------------------------------------------------------
        # any_item : 
        #   can be anything acceptable for python for loop
        # any_store :
        #   can be anything acceptable for python for loop 
        #   in accordance with any_item
        # do_anything :
        #   do_anything is any python command as required by situation
        # return_item :
        #   this must be a variable that is usable to return
        $start
        for $item in $list_or_dict:
            $do_cmd
        $end
        ------------------------------------------------------------------
        command frame keywords : start, item, list_or_dict, do_cmd, end
        """
        ins_15 = CL([testdir_CommandLibraryTest])
        a = ins_15.test_file_1.runGeneratedCode({
                                                 'item':'i',
                                                 'list_or_dict':'range(10)',
                                                 'do_cmd' : 'number += i', 
                                                 'start' : 'number=0', 
                                                 'end': 'self.return_vals = number'
                                                })
        assert a == 45

    def test_CommandLibrary_runGeneratedCode__WriteToAFile(self):
        """check if the runGeneratedCode is working fine. In this test, a new file 
        is written with specific value
        
        Command Frame Files : test_file_3 (this is the command executed by 
        runGeneratedCode)
        ------------------------------------------------------------------
        with open("$filepath", "w") as f:
            f.write("$txt")
        ------------------------------------------------------------------
        command frame keywords : filepath, txt
        """
        ins_14 = CL([testdir_CommandLibraryTest])
        txt_2_write = "I am from the class test_CommandLibrary.py"
        ins_14.runGeneratedCode(ins_14.test_file_3,
                                {
                                'filepath' : testdir_CommandLibraryTest2+"/test_file_3",
                                'txt' : txt_2_write
                                }
                               )
        readTxt = ""
        with open(testdir_CommandLibraryTest2+"/test_file_3", "r") as f:
            readTxt = f.read()
        assert readTxt == txt_2_write


    def test_CommandLibrary_runGeneratedCode_ForLoop(self):
        """check if the runGeneratedCode is working fine. In this test, just 
        checking if for loop works
        
        Command Frame Files : test_file_1 (this is the command executed by 
        runGeneratedCode)
        ------------------------------------------------------------------
        # any_item : 
        #   can be anything acceptable for python for loop
        # any_store :
        #   can be anything acceptable for python for loop 
        #   in accordance with any_item
        # do_anything :
        #   do_anything is any python command as required by situation
        # return_item :
        #   this must be a variable that is usable to return
        $start
        for $item in $list_or_dict:
            $do_cmd
        $end
        ------------------------------------------------------------------
        command frame keywords : start, item, list_or_dict, do_cmd, end
        """
        ins_15 = CL([testdir_CommandLibraryTest])
        a = ins_15.runGeneratedCode(ins_15.test_file_1,
                                    {
                                     'item'        : 'i',
                                     'list_or_dict': 'range(10)',
                                     'do_cmd'      : 'number += i', 
                                     'start'       : 'number=0', 
                                     'end'         : 'self.return_vals = number'
                                    }
                                   )
        assert a == 45

    def test_CommandLibrary_runGeneratedCode_SimpleForLoop(self):
        """check if the runGeneratedCode is working fine. In this test, just 
        checking if for loop works
        
        Command Frame Files : test_file_1 (this is the command executed by 
        runGeneratedCode)
        ------------------------------------------------------------------
        # start : 
        #   just initialize or do anything that is required
        # list_or_dict :
        #   can be a python list or dict 
        # do_cmd :
        #   anything that is needed to be done in for loop
        #   keep it single string for simplicity
        #   if want to use multi-string, consider proper indentation
        # return_item :
        #   this must be a variable that is usable to return
        $start
        for i, item in enumerate($list_or_dict):
            $do_cmd
        $end
        ------------------------------------------------------------------
        command frame keywords : start, item, list_or_dict, do_cmd, end
        """
        ins_15 = CL([testdir_CommandLibraryTest2])
        a = ins_15.runGeneratedCode(ins_15.test_file_4,
                                    {
                                     'start'       : 'self.return_vals=0',
                                     'list_or_dict': 'range(10)',
                                     'do_cmd'      : 'self.return_vals += i'
                                    }
                                   )
        assert (a == 45) & (ins_15.return_vals == 45)






















