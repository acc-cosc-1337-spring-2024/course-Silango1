import unittest

'''
This file has the /src/homework/c_decisions folder.
the function get_options_ratio.
'''
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio_1(self):
        #Test that get_options_ration with values 5 and 20 returns the value .25

        option = 5
        total = 20
        expected_ratio = 0.25
        self.assertEqual(get_options_ratio(option,total),expected_ratio)
    
    def test_get_options_ratio_2(self):
        #Test that get_options_ration with values 10 and 20 returns the value .5.
        option = 10
        total = 20
        expected_ratio = 0.5
        self.assertEqual(get_options_ratio(option,total),expected_ratio)
       
    def test_get_faculty_rating_excellent(self):
        #Test that the function returns ‘Excellent’ when the rating is .91.
        
        rating = 0.91
        expected_result = "Excellent"
        self.assertEqual(get_faculty_rating(rating), expected_result)

    def test_get_faculty_rating_Very_Good(self):
    #Test that the function returns very good when the rating is .85.
        rating = 0.85
        expected_result = "Very Good"
        self.assertEqual(get_faculty_rating(rating),expected_result)

    def test_get_faculty_rating_Good(self):
         #Test that the function returns good when the rating is .71.
        rating = 0.71
        expected_result = "Good"
        self.assertEqual(get_faculty_rating(rating),expected_result)

    def test_get_faculty_rating_Needs_Improvement(self):
         #Test that the function returns needs improvement when the rating is .66.
        rating = 0.66
        expected_result = "Needs Improvement"
        self.assertEqual(get_faculty_rating(rating),expected_result)

    def test_get_faculty_rating_Unacceptable(self):
         #Test that the function returns "unacceptable" when the rating is .45.
        rating = 0.45
        expected_result = "Unacceptable"
        self.assertEqual(get_faculty_rating(rating),expected_result)
    if __name__ == '__main__':
      unittest.main()