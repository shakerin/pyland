#!/usr/bin/python3
PROJECT_DIR = "/mnt/c/work/py-land/"
testdir_common_func = PROJECT_DIR + "pyland/tests/test_examples/common_funcs"
testdir_TemplateLibraryTest = PROJECT_DIR + "pyland/tests/test_examples/testdir_TemplateLibraryTest"
testdir_TemplateLibraryTest2 = PROJECT_DIR + "pyland/tests/test_examples/testdir_TemplateLibraryTest2"
testdir_Discrete_Examples = PROJECT_DIR + "pyland/tests/test_examples/testdir_Discrete_Examples"
testdir_Expected_Output_Examples = PROJECT_DIR + "pyland/tests/test_examples/testdir_Expected_Output_Examples"
tests = PROJECT_DIR + "pyland/tests/test_examples/"
testdir_CommandLibraryTest = PROJECT_DIR + "pyland/tests/test_examples/testdir_CommandLibraryTest"
testdir_CommandLibraryTest2 = PROJECT_DIR + "pyland/tests/test_examples/testdir_CommandLibraryTest2"
# following directory name should be used in testcases, when test
# developer wants the directory to be deleted just after method
# execution. this is currently only cleanable by clean script
delete_after_method_dir = "to_be_deleted"
# following directory name should be used in testcases, when test
# developer wants the directory to be deleted after running clean
# script. this is currently implemented on the system
delete_by_clean_dir = "to_be_deleted"

