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
        """check if createFileIfNotPresent method is working
        properly in this environment.
        
        This test checks two features of the task-
        (i)  file is created when not present
        (ii) file is not created if already present
        """
        dir_path = PV_testdir_common_func + "/" + PV_delete_by_clean_dir
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
      


    def test_getUniqueOrderedList(self):
        """checking getUniqueOrderedList method by providing
        different types of lists
        """
        assert_check = True
        assert_check &= getUniqueOrderedList([1, 2, 5, 10]) == [1, 2, 5, 10]
        assert_check &= getUniqueOrderedList([1, 2, 1, 10]) == [1, 2, 10]
        assert_check &= getUniqueOrderedList([1, 2, 5, 1]) == [1, 2, 5]
        assert_check &= getUniqueOrderedList([1, 2, 5, "a"]) == [1, 2, 5, "a"]
        assert_check &= getUniqueOrderedList(["a", 2, 5, "a"]) == ["a", 2, 5]
        assert assert_check == True


    def test_getOnlyUniqueItems(self):
        """ checking getOnlyUniqueItems method by providing
        different type of lists as argument
        """
        assert_check = True
        assert_check &= getOnlyUniqueItems([1, 2], [2, 3])==[1]
        assert_check &= getOnlyUniqueItems([1, 1], [2, 3])==[1, 1]
        assert_check &= getOnlyUniqueItems([2, 3], [1, 2])==[3]
        assert_check &= getOnlyUniqueItems([1, "1"], ["2", 3, "1"])==[1]
        assert assert_check == True



        
        