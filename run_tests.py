# run_tests.py

import unittest
from tests.homework.e_functions import tests_functions

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
    unittest.TextTestRunner(verbosity=2).run(suite)
