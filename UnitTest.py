import unittest
from unittest.mock import patch
import AddTwoNumbers  # Assuming AddTwoNumbers is the module containing the function to test
from canvasapi import Canvas

# Set your Canvas API URL and access token
API_URL = "https://canvas.instructure.com"
API_KEY = "7~HQHh2VDGNE4gqb7Y5jSWDxcpzGPQDbuIavwlAC3jqFug2EUWaIVK5mGhtX1NEI4D"
canvas = Canvas(API_URL, API_KEY)
course_id = 8817863
assignment_id = 44365116
course = canvas.get_course(course_id)
assignment = course.get_assignment(assignment_id)
submission = assignment.get_submission(AddTwoNumbers.student_id)

class TestAddTwoInputs(unittest.TestCase):
    total = 0  # Define total as a class variable

    @patch('builtins.input', side_effect=['2', '3'])
    def test_addTwoInputs_case1(self, mock_input):
        result1 = AddTwoNumbers.test()  # Assuming there's a function named test in AddTwoNumbers module
        self.assertEqual(result1, 5, "Test case 1 failed: Expected sum 5")
        TestAddTwoInputs.total += 5  # Update total for each test case

    @patch('builtins.input', side_effect=['-1', '5'])
    def test_addTwoInputs_case2(self, mock_input):
        result2 = AddTwoNumbers.test()  # Assuming there's a function named test in AddTwoNumbers module
        self.assertEqual(result2, 4, "Test case 2 failed: Expected sum 4")
        TestAddTwoInputs.total += 5  # Update total for each test case

if __name__ == '__main__':
    # Run the tests
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestAddTwoInputs))
    
    # Check if all tests passed or not
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")
    
    # Print total
    print("Total:", TestAddTwoInputs.total)
    submission.edit(submission={'posted_grade': TestAddTwoInputs.total})
    
