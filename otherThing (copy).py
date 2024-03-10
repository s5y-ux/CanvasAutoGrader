import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def generate_run_program(test_cases):
    # Collect unique test methods
    unique_methods = set(test_case['test_method'] for test_case in test_cases)
    methods = "\n".join([f"    print(Assignment.{method}())" for method in unique_methods])
    code = f"""# Used to import the Assignment file
import Assignment

# Main Body
if __name__ == "__main__":
{methods}"""
    return code

def generate_code_and_student_id(test_cases):
    # Collect unique test methods
    unique_methods = set(test_case['test_method'] for test_case in test_cases)
    methods = "\n".join([f"def {method}():\n    pass" for method in unique_methods])
    code = f"""# Please put your student ID here: (Not your 900 number)
student_id = 0

{methods}
"""
    return code

def generate_test_program(API_URL, API_KEY, course_id, assignment_id, test_cases):
    # Generating the Python program dynamically
    code = f"""
import unittest
from unittest.mock import patch
import Assignment
from canvasapi import Canvas

API_URL = "{API_URL}"
API_KEY = "{API_KEY}"
canvas = Canvas(API_URL, API_KEY)
course_id = {course_id}
assignment_id = {assignment_id}
course = canvas.get_course(course_id)
assignment = course.get_assignment(assignment_id)
submission = assignment.get_submission(Assignment.student_id)

class TestAddTwoInputs(unittest.TestCase):
    total = 0

"""

    # Adding test cases dynamically
    for i, test_case in enumerate(test_cases, start=1):
        inputs = ", ".join(map(repr, test_case["inputs"]))
        expected_output = repr(test_case["expected_output"])
        test_method = test_case["test_method"]
        points = test_case["points"]
        code += f"""
    @patch('builtins.input', side_effect=[{inputs}])
    def test_addTwoInputs_case{i}(self, mock_input):
        result = Assignment.{test_method}()
        self.assertEqual(result, {expected_output}, "Test case {i} failed: Expected output {expected_output}")
        TestAddTwoInputs.total += {points}

"""

    # Adding the main block
    code += """
if __name__ == '__main__':
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestAddTwoInputs))
    
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")
    
    print("Total:", TestAddTwoInputs.total)
    submission.edit(submission={'posted_grade': TestAddTwoInputs.total})
"""

    return code


def generate_program():
    # Get values from entry fields
    api_url = api_url_entry.get()
    api_key = api_key_entry.get()
    course_id = int(course_id_entry.get())
    assignment_id = int(assignment_id_entry.get())
    folder_path = folder_path_var.get()

    # Parse test cases
    test_cases = []
    for case_entry in test_cases_entries:
        inputs = eval(case_entry['inputs'].get())
        expected_output = eval(case_entry['expected_output'].get())
        test_method = case_entry['test_method'].get()
        points = int(case_entry['points'].get())
        test_cases.append({"inputs": inputs, "expected_output": expected_output, "test_method": test_method, "points": points})

    # Generate the test program
    generated_code = generate_test_program(api_url, api_key, course_id, assignment_id, test_cases)

    # Output generated code to a file in the specified folder
    file_name = os.path.join(folder_path, "Grade.py")
    with open(file_name, 'w') as f:
        f.write(generated_code)
    
    other_file_name = os.path.join(folder_path, "Assignment.py")
    with open(other_file_name, 'w') as r:
        r.write(generate_code_and_student_id(test_cases))

    run_file_name = os.path.join(folder_path, "Run.py")
    with open(run_file_name, 'w') as r:
        r.write(generate_run_program(test_cases))

    text_file_name = os.path.join(folder_path, "IMPORTANT.txt")
    with open(text_file_name, 'w') as r:
        r.write("Please run \"python -OO -m py_compile Grade.py\" and pull the compiled code out of the pycache and delete Grade.py...")


def add_test_case():
    # Add entry fields for a new test case
    case_frame = ttk.Frame(test_cases_frame)
    case_frame.grid(row=len(test_cases_entries), column=0, padx=5, pady=5)

    inputs_label = ttk.Label(case_frame, text="Inputs:")
    inputs_label.grid(row=0, column=0, padx=5, pady=5)
    inputs_entry = ttk.Entry(case_frame, width=20)
    inputs_entry.grid(row=0, column=1, padx=5, pady=5)
    inputs_entry.insert(0, "[2, 3]")

    expected_output_label = ttk.Label(case_frame, text="Expected Output:")
    expected_output_label.grid(row=0, column=2, padx=5, pady=5)
    expected_output_entry = ttk.Entry(case_frame, width=10)
    expected_output_entry.grid(row=0, column=3, padx=5, pady=5)
    expected_output_entry.insert(0, "5")

    test_method_label = ttk.Label(case_frame, text="Test Method:")
    test_method_label.grid(row=0, column=4, padx=5, pady=5)
    test_method_entry = ttk.Entry(case_frame, width=10)
    test_method_entry.grid(row=0, column=5, padx=5, pady=5)
    test_method_entry.insert(0, "test")

    points_label = ttk.Label(case_frame, text="Points:")
    points_label.grid(row=0, column=6, padx=5, pady=5)
    points_entry = ttk.Entry(case_frame, width=5)
    points_entry.grid(row=0, column=7, padx=5, pady=5)
    points_entry.insert(0, "5")

    test_cases_entries.append({
        "inputs": inputs_entry,
        "expected_output": expected_output_entry,
        "test_method": test_method_entry,
        "points": points_entry
    })

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

# Create tkinter window
root = tk.Tk()

root.title("Python Assignment Generator")
root.geometry("600x650")  # Adjusted window size for better layout

# Style configuration
style = ttk.Style(root)
style.theme_use('clam')  # Using a theme that's typically more visually appealing than the default

# Font configuration
style.configure('TLabel', font=('Arial', 10))
style.configure('TButton', font=('Arial', 10, 'bold'), background='lightblue')
style.configure('TEntry', font=('Arial', 10), padding=5)

# Improved layout with consistent padding and margins
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.pack(fill='x', expand=True)

# Widget definitions continue here, with improved padding and layout adjustments...


# Frame to hold input fields
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Labels and entry fields for API parameters
api_url_label = ttk.Label(input_frame, text="API URL:")
api_url_label.grid(row=0, column=0, padx=5, pady=5)
api_url_entry = ttk.Entry(input_frame, width=30)
api_url_entry.grid(row=0, column=1, padx=5, pady=5)
api_url_entry.insert(0, "https://canvas.instructure.com")

api_key_label = ttk.Label(input_frame, text="API Key:")
api_key_label.grid(row=1, column=0, padx=5, pady=5)
api_key_entry = ttk.Entry(input_frame, width=30)
api_key_entry.grid(row=1, column=1, padx=5, pady=5)

course_id_label = ttk.Label(input_frame, text="Course ID:")
course_id_label.grid(row=2, column=0, padx=5, pady=5)
course_id_entry = ttk.Entry(input_frame, width=30)
course_id_entry.grid(row=2, column=1, padx=5, pady=5)

assignment_id_label = ttk.Label(input_frame, text="Assignment ID:")
assignment_id_label.grid(row=3, column=0, padx=5, pady=5)
assignment_id_entry = ttk.Entry(input_frame, width=30)
assignment_id_entry.grid(row=3, column=1, padx=5, pady=5)

# Frame to hold test cases input fields
test_cases_frame = ttk.LabelFrame(root, text="Test Cases")
test_cases_frame.pack(pady=10)

test_cases_entries = []

# Add entry fields for initial test cases
for i in range(2):  # Example: creating 2 entry fields for test cases
    add_test_case()

# Button to add more test cases
add_case_button = ttk.Button(root, text="Add Test Case", command=add_test_case)
add_case_button.pack(pady=5)

# Button to browse folder
browse_button = ttk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=5)

# Variable to hold folder path
folder_path_var = tk.StringVar()
folder_path_label = ttk.Label(root, text="Select Folder:")
folder_path_label.pack(pady=5)
folder_path_entry = ttk.Entry(root, textvariable=folder_path_var, width=30, state='readonly')
folder_path_entry.pack(pady=5)

# Button to generate the program
generate_button = ttk.Button(root, text="Generate Assignment", command=generate_program)
generate_button.pack(pady=10)

root.geometry("1200x600")

root.mainloop()
