#!/usr/bin/python3

import pytest
from string import Template
from docopt import docopt
import re
from os.path import join
import os
import filecmp

from ucg.TemplateInfo import TemplateInfo as TI
from ucg.FileToTemplate import FileToTemplate as FTT
from ucg.TemplateLibrary import TemplateLibrary as TL
from ucg.Structure import Structure
from ucg.Pyland import Pyland
from tests.path_variables import *



class TestPyland:

    
    structure_file_path_main = PV_testdir_Structure + "/pyland_main.struct"
    frame_dirs = [PV_testdir_Frames]
    pyland_main = Pyland(frame_dirs, structure_file_path_main)


    
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
                                                        ('FILE', 'to_be_deleted_test1/file1.txt', "justText{'arg':'FILE1_FROM_TEST1'}"),
                                                        ('FILE', 'to_be_deleted_test1/file2.txt', "justText{'arg':'FILE2_FROM_TEST1'}"),
                                                        ('FILE', 'to_be_deleted_test1/file3.txt', "justText{'arg':'FILE3_FROM_TEST1'}"),
                                                        ('FILE', 'to_be_deleted_test1/test2/file1.txt', "justText{'arg':'FILE1_FROM_TEST1/TEST2'}"),
                                                        ('FILE', 'to_be_deleted_test1/test2/file2.txt', "justText{'arg':'FILE2_FROM_TEST1/TEST2'}"),
                                                        ('FILE', 'to_be_deleted_test1/test2/file3.txt', "justText{'arg':'FILE3_FROM_TEST1/TEST2'}"),
                                                        ])


    def test_Pyland_CMDnames(self):
        assert (TestPyland.pyland_main.ST1.cmd_names) ==  ([
                                                                "abc",
                                                                "justText{'arg':'FILE1_FROM_TEST1'}",
                                                                "justText{'arg':'FILE2_FROM_TEST1'}",
                                                                "justText{'arg':'FILE3_FROM_TEST1'}",
                                                                "",
                                                                "justText{'arg':'FILE1_FROM_TEST1/TEST2'}",
                                                                "justText{'arg':'FILE2_FROM_TEST1/TEST2'}",
                                                                "justText{'arg':'FILE3_FROM_TEST1/TEST2'}",
                                                                "",
                                                                "",
                                                                "",
                                                                "",
                                                                ])


    def test_Pyland_Structure_CommadExec(self):
        read_data = []
        for file_path in TestPyland.pyland_main.ST1.file_paths:
            with open(file_path) as f:
                data = f.read()
                read_data.append(data)
        assert read_data == [
                            "This is just Text\nArgument from Struct file is : FILE1_FROM_TEST1",
                            "This is just Text\nArgument from Struct file is : FILE2_FROM_TEST1",
                            "This is just Text\nArgument from Struct file is : FILE3_FROM_TEST1",
                            "This is just Text\nArgument from Struct file is : FILE1_FROM_TEST1/TEST2",
                            "This is just Text\nArgument from Struct file is : FILE2_FROM_TEST1/TEST2",
                            "This is just Text\nArgument from Struct file is : FILE3_FROM_TEST1/TEST2",
                            ]

    def test_Pyland_Frame_CommadExec(self):
        frame_cmd = "justText{'arg':'FILE1_FROM_TEST1/TEST2'}"
        pyland_ins = Pyland(TestPyland.frame_dirs, frame_cmd)
        assert pyland_ins.frame_generated_code == "This is just Text\nArgument from Struct file is : FILE1_FROM_TEST1/TEST2"
        
    def test_Pyland_Frame_CommadExec_with_outputfile(self):
        frame_cmd = "justText{'arg':'FILE1_FROM_TEST1/TEST2'}"
        outputfilepath = PV_testdir_Structure + "/to_be_deleted/to_be_deleted_test1.txt"
        pyland_ins = Pyland(TestPyland.frame_dirs, frame_cmd, outputfilepath)
        with open(outputfilepath) as f:
            output = f.read()
        assert pyland_ins.frame_generated_code == output

    def test_Pyland_Frame_WrongCommadExec(self):
        frame_cmd = "justTextFILE1_FROM_TEST1/TEST2'}"
        pyland_ins = Pyland(TestPyland.frame_dirs, frame_cmd)
        expected_output = "PYLAND(execFileCmd): FRAME NOT PRESENT : " + frame_cmd
        assert pyland_ins.frame_generated_code == expected_output

    def test_Pyland_Frame_WrongCommadExec_with_outputfile(self):
        frame_cmd = "justTextFILE1_FROM_TEST1/TEST2'}"
        expected_output = "PYLAND(execFileCmd): FRAME NOT PRESENT : " + frame_cmd
        outputfilepath = PV_testdir_Structure + "/to_be_deleted/to_be_deleted_test1.txt"
        pyland_ins = Pyland(TestPyland.frame_dirs, frame_cmd, outputfilepath)
        with open(outputfilepath) as f:
            output = f.read()
        assert expected_output == output





    def test_auto_structure_test(self):
        # create Pyland instance for frame_dirs and struct file
        autotest_frame = PV_testdir_Structure + "/Autotest_frame_files"
        autotest_frame_dirs = [autotest_frame]

        autotest_struct = PV_testdir_Structure + "/Autotest_struct_files/check_all_frames.struct"

        autotest_struct_output = PV_testdir_Structure + "/Autotest_struct_output_files"


        # Pyland instance creation
        pyland_auto_frame_test = Pyland(autotest_frame_dirs, autotest_struct)
        created_file_paths = pyland_auto_frame_test.ST1.file_paths

        output_file_paths = [autotest_struct_output+"/"+filepath.split('/')[-1]  for filepath in created_file_paths]

        # read the struct file to collect file locations and names
        matched = True
        for created_file, output_file in zip(created_file_paths, output_file_paths):
            matched &= filecmp.cmp(created_file, output_file)
            if not matched:
                print(created_file.split('/')[-1])
                break
        assert matched == True



