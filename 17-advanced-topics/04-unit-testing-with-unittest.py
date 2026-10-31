# ----------------------------------------------------
# -- Advanced Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# ----------------------------------------------------
# unitest
# - Add Tests Into Classes As Methods
# - Use A Seris Of Special Assertion Methods
# https://docs.python.org/3/library/unitest.html
# ----------------------------------------------


# assert 3*8 == 23, "Should Be 24"  # AssertionErrord

# def test_case_one():
    
#     assert 5*10 == 50, "Should Be 50"
    
# def test_case_two():
    
#     assert 5*50 == 250, "Should Be 250"
    
# if __name__ == "__main__" :
    
#     test_case_one()
    
#     test_case_two()
    
#     print("All Tests Passed")

import unittest

class MyTestCase(unittest.TestCase):
    
    def test_one(self):
        
        self.assertTrue(100 > 99 , "Should Be True")
        
    
    def test_two(self):
        
        self.assertEqual(40 + 60, 100, "Sould Be 100")
        
        
    def test_three(self):
        
        self.assertGreater(100, 180, "Should Be True")
        

if __name__ == "__main__" :
    
    unittest.main()
    
 