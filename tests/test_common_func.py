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
        """
        dir_name = "/to_be_deleted"
        dir_path = testdir_common_func + dir_name
        dir_initially_present = os.path.isdir(dir_path)
        createDirIfNotPresent(dir_path)
        dir_created = os.path.isdir(dir_path)
        dir_already_present = createDirIfNotPresent(dir_path)
        assert (dir_initially_present==False) and \
                (dir_created==True) and \
                (dir_already_present==True)
        if dir_already_present:
            os.rmdir(dir_path)
        return
        


        
        