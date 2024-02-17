import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#aDDING IMPORT FOR MULTIPLY NUMBERS
from tests.homework.d_repetition import tests_repetition

#Verify the change
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)
