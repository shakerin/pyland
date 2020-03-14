#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
import os
from os.path import join

from .context import *
from .path_variables import *

class TestTemplateLibrary:
    """test name format : test_{className/methodName}_{unit_for_test}"""
    ins_TL_1 = TL([PV_testdir_TemplateLibrary_FrameFiles])
    ins_TL_2 = TL([PV_testdir_TemplateLibrary_FrameFiles_2])
    ins_TL_all = TL([PV_testdir_TemplateLibrary_FrameFiles,PV_testdir_TemplateLibrary_FrameFiles_2])

    def insTL1FrameInfos(self):
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        return (expected_list, filenames)


    def insTLAllFrameInfos(self):
        expected_list, filenames1 = [], []
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles):
            filenames1 = files
            for filename in files:
                expected_list.append(os.path.join(root, filename))
        for root, dirs, files in os.walk(PV_testdir_TemplateLibrary_FrameFiles_2):
            filename2 = files
            for filename in files:
                if filename not in filenames1:
                    expected_list.append(os.path.join(root, filename))
        filenames1.extend(filename2)
        filenames = list(dict.fromkeys(filenames1))
        return (expected_list, filenames)

    def removeFileExtension(self, file_names):
        expected_frame_names = []
        for frame_name in file_names:
            if "." in frame_name:
                expected_frame_name = frame_name.split(".")[0]
            else:
                expected_frame_name = frame_name
            expected_frame_names.append(expected_frame_name)
        return expected_frame_names

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
        ins_TL_all_framepaths, frame_names = self.insTLAllFrameInfos()
        assert sorted(ins_TL_all_framepaths) == sorted(TestTemplateLibrary.ins_TL_all.frame_files)

    def test_TemplateLibrary_loadAllTemplates_frame_names(self):
        """check the internal list frame_name after creating TL object with path"""
        file_paths, file_names = self.insTLAllFrameInfos()
        expected_frame_names = self.removeFileExtension(file_names)
        assert sorted(expected_frame_names) == sorted(TestTemplateLibrary.ins_TL_all.frame_names)

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectInternalVariable_name(self):
        """test the internal variable 'name' that is stored in frame object
        matches the file name string until file extension"""
        assert "test_file_1" == TestTemplateLibrary.ins_TL_all.test_file_1.name

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectsCreated(self):
        """check which frame objects are created from the frame directory"""
        expected_list, filenames = self.insTL1FrameInfos()
        expected_frame_names = self.removeFileExtension(filenames)
        assert sorted(TestTemplateLibrary.ins_TL_1.frame_names) == sorted(expected_frame_names)

    def test_TemplateLibrary_loadAllTemplates_ListOfFrameFiles(self):
        """check the file paths of the created frame objects are correct"""
        expected_list, filenames = self.insTL1FrameInfos()
        expected_frame_names = self.removeFileExtension(filenames)
        assert sorted(TestTemplateLibrary.ins_TL_1.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_loadAllTemplates_DynamicObjects_FrameLocationSearch(self):
        """check the method for searching particular frame object is correct"""
        assert TestTemplateLibrary.ins_TL_all.findFrame("test_file_6") == PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_6" 

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectInternalVariable_key_words(self):
        """test the internal variable 'key_words' that is stored in frame object
        matches the actual number of keywords in frame file"""
        assert sorted(TestTemplateLibrary.ins_TL_all.test_file_1.key_words) == sorted(["number", "name"])

    def test_TemplateLibrary_loadAllTemplates_DynamicObjectsUsage(self):
        """check the generated text from particular frame object is correct"""
        generated_code = TestTemplateLibrary.ins_TL_1.test_file_2.getGeneratedCode({
                                                             'word':'FILE',
                                                             'check':'TEST'
                                                             })
        assert generated_code == "this is single FILE framefile just to TEST"

    def test_TemplateLibrary_getGeneratedCode_DynamicObjectsUsage(self):
        """check the generated text from particular frame object is correct, this 
        getGenerateCode is accessible from TemplateLibrary"""
        generated_code = TestTemplateLibrary.ins_TL_1.getGeneratedCode(TestTemplateLibrary.ins_TL_1.test_file_2,
                                                {
                                                'word':'FILE',
                                                'check':'TEST'
                                                }
                                               )
        assert generated_code == "this is single FILE framefile just to TEST"

    def test_TemplateLibrary_loadAllTemplates_addFrameDirs_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_11= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_11.addFrameDirs([PV_testdir_TemplateLibrary_FrameFiles_2])
        expected_list, filenames = self.insTLAllFrameInfos()
        assert sorted(ins_11.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_loadAllTemplates_addFrameFromFile_TrueCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_12= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_12.addFrameFromFile(PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_4.txt")
        expected_list, filenames = self.insTL1FrameInfos()
        expected_list.append(PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_4.txt")
        assert sorted(ins_12.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_loadAllTemplates_addFrameFromFile_FalseCheck(self):
        """check number of frames are same when all frame_dirs are 
        included in the class object and thus the method addFrameDirs is
        working fine tested"""
        ins_13= TL([PV_testdir_TemplateLibrary_FrameFiles])
        ins_13.addFrameFromFile(PV_testdir_TemplateLibrary_FrameFiles_2 + "/test_file_10.txt")
        expected_list, filenames = self.insTL1FrameInfos()
        assert sorted(ins_13.frame_files)==sorted(expected_list)

    def test_TemplateLibrary_frameObj_withExecSegments_getGeneratedCode(self):
        """check the generated text from particular frame object is correct"""
        generated_code = TestTemplateLibrary.ins_TL_1.getGeneratedCode(TestTemplateLibrary.ins_TL_1.frame_with_exec_seg_assign_var,
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
        execSections = TestTemplateLibrary.ins_TL_1.frame_with_exec_seg_assign_var.exec_sections
        expected_output = ['self.txt = "I am a txt generated from $name class"\n']
        assert execSections == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_modified_string(self):
        """check the generated text from particular frame object is correct"""
        modified_string = TestTemplateLibrary.ins_TL_1.frame_with_exec_seg_assign_var.modified_string
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var_modified_string.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert modified_string == expected_output

    def test_TemplateLibrary_frameObj_withExecSegments_runExecSection(self):
        """check the generated text from particular frame object is correct"""
        output = TestTemplateLibrary.ins_TL_1.runExecSection('self.txt = "I am Executed Text"')
        assert output == "I am Executed Text"

    def test_TemplateLibrary_frameObj_withExecSegments_runExecSections_1(self):
        """check the generated text from particular frame object is correct"""
        exec_strings_list = [
            'self.txt = "I am Executed Text 1"',
            'self.txt = "I am Executed Text 2"'
        ]
        output = TestTemplateLibrary.ins_TL_1.runExecSections(exec_strings_list)
        expected_output = [
            'I am Executed Text 1',
            'I am Executed Text 2'
        ]
        assert sorted(output) == sorted(expected_output)

    def test_TemplateLibrary_frameObj_withExecSegments_runExecSections_2(self):
        """check the generated text from particular frame object is correct"""
        exec_strings_list = [
            'self.txt = "I am Executed Text 1"',
            'print("I am Executed Text 2")'
        ]
        output = TestTemplateLibrary.ins_TL_1.runExecSections(exec_strings_list)
        expected_output = [
            'I am Executed Text 1',
            ''
        ]
        assert sorted(output) == sorted(expected_output)

    def test_TemplateLibrary_frameObj_withExecSegments_getAll_1(self):
        """check the generated text from particular frame object is correct"""
        generated_code = TestTemplateLibrary.ins_TL_1.getAll(TestTemplateLibrary.ins_TL_1.frame_with_exec_seg_assign_var,
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
        generated_code = TestTemplateLibrary.ins_TL_1.getAll(TestTemplateLibrary.ins_TL_1.frame_with_exec_seg_assign_var_version2,
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
        modified_string = TestTemplateLibrary.ins_TL_all.frame_with_exec_seg_assign_var_version2.modified_string
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_assign_var_modified_string_2.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert modified_string == expected_output


    def test_TemplateLibrary_frameObj_withExecSegments_getAll_3(self):
        """check the generated text from particular frame object is correct
        in this frame, local and global variables are used"""
        generated_code = TestTemplateLibrary.ins_TL_1.getAll(TestTemplateLibrary.ins_TL_1.frame_with_exec_seg_variable_check,
                                      {})
        output_file_path = PV_testdir_TemplateLibrary_FrameFilesOutput + \
                           "/example_frame_with_exec_seg_variable_check.txt" 
        expected_output = ""
        with open(output_file_path, 'r') as f:
            expected_output = f.read()
        assert generated_code == expected_output