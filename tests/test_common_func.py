#!/usr/bin/python3

import pytest
import os
import shutil
from tests.path_variables import *
from ucg.common_func import *


class TestCommonFunc:
    """This class is for testing all functions inside common_func.py"""

    def test_createDirIfNotPresent(self):
        """check if createDirIfNotPresent method is working
        properly in this environment.
        
        This test checks two features of the task-
        (i)  directory is created when not present
        (ii) directory is not created if already present
        """
        dir_path = PV_testdir_common_func + "/" + PV_delete_by_clean_dir
        # checks if directory already present
        dir_initially_present = os.path.isdir(dir_path)
        createDirIfNotPresent(dir_path)
        dir_created = os.path.isdir(dir_path)
        # trying to re-create directory
        dir_already_present = createDirIfNotPresent(dir_path)
        assert (dir_initially_present==False) and \
                (dir_created==True) and \
                (dir_already_present==True)
        if dir_already_present:
            os.rmdir(dir_path)
        return


    
    def test_createFileIfNotPresent(self):
        dir_path = PV_testdir_common_func + "/" + PV_delete_by_clean_dir
        createDirIfNotPresent(dir_path)
        file_path = dir_path + "/createFileIfNotPresentTest.txt"
        # checks if file already present
        file_initially_present = os.path.isfile(file_path)
        createFileIfNotPresent(file_path)
        file_created = os.path.isfile(file_path)
        # trying to re-create file
        file_already_present = createFileIfNotPresent(file_path)
        assert (file_initially_present==False) and \
                (file_created==True) and \
                (file_already_present==True)
        if file_already_present:
            os.remove(file_path)

        return
      


        
        