#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
import os
from os.path import join

from ucg.TemplateInfo import TemplateInfo as TI
from ucg.FileToTemplate import FileToTemplate as FTT
from ucg.TemplateLibrary import TemplateLibrary as TL
from tests.path_variables import *

class TestTemplateLibrary:
    """test name format : test_{className/methodName}_{unit_for_test}"""

    def test_TemplateLibrary_loadFrameFilesFromDir_frame_dirs(self):
        """check the internal list frame_dirs after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = TL()
        ins.loadFrameFilesFromDir(PV_testdir_TemplateLibrary_FrameFiles)
        expected_frame_dirs = []
        assert expected_frame_dirs == ins.frame_dirs

    def test_TemplateLibrary_frame_dirs(self):
        """this test checks if the frame_dirs are stored properly or not."""
        ins_22= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_22.addFrameDirs([PV_testdir_TemplateLibrary_FrameFiles_2])
        exp_frame_dirs = [
            PV_testdir_TemplateLibrary_FrameFiles,
            PV_testdir_TemplateLibrary_FrameFiles_2
        ]
        assert sorted(ins_22.frame_dirs)==sorted(exp_frame_dirs)

    def test_TemplateLibrary_frame_dirs_CheckOneDirIsNotAddedTwice(self):
        """this test checks if the frame_dirs are stored properly or not."""
        ins_22= TL([PV_testdir_TemplateLibrary_FrameFiles, 
                    PV_testdir_TemplateLibrary_FrameFiles_2])
        ins_22.addFrameDirs([PV_testdir_TemplateLibrary_FrameFiles_2])
        exp_frame_dirs = [
            PV_testdir_TemplateLibrary_FrameFiles,
            PV_testdir_TemplateLibrary_FrameFiles_2
        ]
        assert sorted(ins_22.frame_dirs)==sorted(exp_frame_dirs)

    def test_TemplateLibrary_loadFrameFilesFromDir_frame_files(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = TL()
        ins.loadFrameFilesFromDir(PV_testdir_TemplateLibrary_FrameFiles)
        expected_list = []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        expected_abspath_list = [join(PV_testdir_TemplateLibrary_FrameFiles, f) for f in expected_list] 
        assert sorted(expected_abspath_list) == sorted(ins.frame_files)

    def test_TemplateLibrary_loadFrameFilesFromDir_frame_names(self):
        """check the internal list frame_files after calling loadFrameFilesFromDir(dir_path)
        method from the object"""
        ins = TL()
        expected_frame_names_raw, expected_frame_names = [], []
        ins.loadFrameFilesFromDir(PV_testdir_TemplateLibrary_FrameFiles)
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            expected_frame_names_raw = files
        for frame_name in expected_frame_names_raw:
            if "." in frame_name:
                expected_frame_name = frame_name.split(".")[0]
            else:
                expected_frame_name = frame_name
            expected_frame_names.append(expected_frame_name)
        assert sorted(expected_frame_names) == sorted(ins.frame_names)

    def test_TemplateLibrary_loadAllTemplates_frame_files(self):
        """check the internal list frame_files after creating TL object with path"""
        ins = TL([PV_testdir_TemplateLibrary_FrameFiles,PV_testdir_TemplateLibrary_FrameFiles_2])
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles_2):
            for filename in files:
                if filename not in filenames1:
                    expected_list.append(os.path.join(root, filename))
        assert sorted(expected_list) == sorted(ins.frame_files)

    def test_TemplateLibrary_loadAllTemplates_frame_names(self):
        """check the internal list frame_name after creating TL object with path"""
        ins_4 = TL([PV_testdir_TemplateLibrary_FrameFiles,PV_testdir_TemplateLibrary_FrameFiles_2])
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
        newfiles = []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles_2):
            for filename in files:
                if filename not in filenames1:
                    newfiles.append(filename)
        filenames1.extend(newfiles)
        expected_frame_names = []
        for frame_name in filenames1:
            if "." in frame_name:
                expected_frame_name = frame_name.split(".")[0]
            else:
                expected_frame_name = frame_name
            expected_frame_names.append(expected_frame_name)
        assert sorted(expected_frame_names) == sorted(ins_4.frame_names)

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectInternalVariable_name(self):
        """test the internal variable 'name' that is stored in frame object
        matches the file name string until file extension"""
        ins_5= TL([PV_testdir_TemplateLibrary_FrameFiles,PV_testdir_TemplateLibrary_FrameFiles_2])
        assert "test_file_1" == ins_5.test_file_1.name

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectsCreated(self):
        """check which frame objects are created from the frame directory"""
        ins_6= TL([PV_testdir_TemplateLibrary_FrameFiles])
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        expected_frame_names = []
        for frame_name in filenames1:
            if "." in frame_name:
                expected_frame_name = frame_name.split(".")[0]
            else:
                expected_frame_name = frame_name
            expected_frame_names.append(expected_frame_name)
        assert sorted(ins_6.frame_names) == sorted(expected_frame_names)

    def test_TemplateLibrary_loadAllTemplates_ListOfFrameFiles(self):
        """check the file paths of the created frame objects are correct"""
        ins_8= TL([PV_testdir_TemplateLibrary_FrameFiles])
        dirpath = PV_testdir_TemplateLibrary_FrameFiles
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))

        assert sorted(ins_8.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_loadAllTemplates_DynamicObjects_FrameLocationSearch(self):
        """check the method for searching particular frame object is correct"""
        ins_9 = TL([PV_testdir_TemplateLibrary_FrameFiles,PV_testdir_TemplateLibrary_FrameFiles_2])
        assert ins_9.findFrame("test_file_6") == PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_6" 

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectInternalVariable_key_words(self):
        """test the internal variable 'key_words' that is stored in frame object
        matches the actual number of keywords in frame file"""
        ins_5= TL([PV_testdir_TemplateLibrary_FrameFiles,PV_testdir_TemplateLibrary_FrameFiles_2])
        assert sorted(ins_5.test_file_1.key_words) == sorted(["number", "name"])

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectsUsage(self):
        """check the generated text from particular frame object is correct"""
        ins_7= TL([PV_testdir_TemplateLibrary_FrameFiles])
        generated_code = ins_7.test_file_2.getGeneratedCode({
                                                             'word':'FILE',
                                                             'check':'TEST'
                                                             })
        assert generated_code == "this is single FILE framefile just to TEST"

    def test_TemplateLibrary_getGeneratedCode_DynamicObjectsUsage(self):
        """check the generated text from particular frame object is correct, this 
        getGenerateCode is accessible from TemplateLibrary"""
        ins_7= TL([PV_testdir_TemplateLibrary_FrameFiles])
        generated_code = ins_7.getGeneratedCode(ins_7.test_file_2,
                                                {
                                                'word':'FILE',
                                                'check':'TEST'
                                                }
                                               )
        assert generated_code == "this is single FILE framefile just to TEST"



    def test_TemplateLibrary_loadAllTemplates_addFrameDirs_FalseCheck(self):
        """check number of frames are different when all frame_dirs are not 
        included in the class object"""
        ins_10= TL([PV_testdir_TemplateLibrary_FrameFiles])
        dirpath = PV_testdir_TemplateLibrary_FrameFiles
        dirpath2 = PV_testdir_TemplateLibrary_FrameFiles_2
        filepaths = [
            dirpath + "/test_file_1.txt",
            dirpath + "/test_file_2.txt",
            dirpath + "/test_file_3",
            dirpath2 + "/test_file_4.txt",
            dirpath2 + "/test_file_5.txt",
            dirpath2 + "/test_file_6",
        ]
        assert sorted(ins_10.frame_files)!=sorted(filepaths)

    def test_TemplateLibrary_loadAllTemplates_addFrameDirs_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_11= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_11.addFrameDirs([PV_testdir_TemplateLibrary_FrameFiles_2])
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles_2):
            for filename in files:
                if filename not in filenames1:
                    expected_list.append(os.path.join(root, filename))
        assert sorted(ins_11.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_loadAllTemplates_addFrameFromFile_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_12= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_12.addFrameFromFile(PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_4.txt")
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        expected_list.append(PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_4.txt")
        assert sorted(ins_12.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_loadAllTemplates_addFrameFromFile_FalseCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_13= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_13.addFrameFromFile(PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_10.txt")
        dirpath = PV_testdir_TemplateLibrary_FrameFiles
        dirpath2 = PV_testdir_TemplateLibrary_FrameFiles_2
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        assert sorted(ins_13.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_frameObj_withExecSegments_getGeneratedCode(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        generated_code = ins_14.getGeneratedCode(ins_14.frame_with_exec_seg_assign_var,
                                                 {
                                                  'name':'EXAMPLE',
                                                  'anything':'FILE',
                                                  'language':'PYTHON'
                                                 })
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert generated_code == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_exec_sections(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        execSections = ins_14.frame_with_exec_seg_assign_var.exec_sections
        expected_output = ['self.txt = "I am a txt generated from $name class"\n']
        assert execSections == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_modified_string(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        modified_string = ins_14.frame_with_exec_seg_assign_var.modified_string
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var_modified_string.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert modified_string == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_runExecSection(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        output = ins_14.runExecSection('self.txt = "I am Executed Text"')
        assert output == "I am Executed Text"

    def test_TemplateLibrary_frameObj_withExecSegments_runExecSections_1(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        exec_strings_list = [
            'self.txt = "I am Executed Text 1"',
            'self.txt = "I am Executed Text 2"'
        ]
        output = ins_14.runExecSections(exec_strings_list)
        expected_output = [
            'I am Executed Text 1',
            'I am Executed Text 2'
        ]
        assert sorted(output) == sorted(expected_output)

    def test_TemplateLibrary_frameObj_withExecSegments_runExecSections_2(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        exec_strings_list = [
            'self.txt = "I am Executed Text 1"',
            'print("I am Executed Text 2")'
        ]
        output = ins_14.runExecSections(exec_strings_list)
        expected_output = [
            'I am Executed Text 1',
            ''
        ]
        assert sorted(output) == sorted(expected_output)

    def test_TemplateLibrary_frameObj_withExecSegments_getAll_1(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        generated_code = ins_14.getAll(ins_14.frame_with_exec_seg_assign_var,
                                      {
                                        'name':'EXAMPLE',
                                        'anything':'FILE',
                                        'language':'PYTHON'
                                       })
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var_executed.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert generated_code == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_getAll_2(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        generated_code = ins_14.getAll(ins_14.frame_with_exec_seg_assign_var_version2,
                                      {
                                        'name':'EXAMPLE',
                                        'anything':'FILE',
                                        'language':'PYTHON'
                                       })
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var_executed_version2.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert generated_code == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_modified_string_2(self):
        """check the generated text from particular frame object is correct"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        modified_string = ins_14.frame_with_exec_seg_assign_var_version2.modified_string
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var_modified_string_2.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert modified_string == expected_output


    def test_TemplateLibrary_frameObj_withExecSegments_getAll_3(self):
        """check the generated text from particular frame object is correct
        in this frame, local and global variables are used"""
        ins_14= TL([PV_testdir_TemplateLibrary_FrameFiles])
        generated_code = ins_14.getAll(ins_14.frame_with_exec_seg_variable_check,
                                      {})
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_variable_check.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert generated_code == expected_output