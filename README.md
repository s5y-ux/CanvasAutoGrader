# CanvasAutoGrader

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Canvas API](https://img.shields.io/badge/Canvas-API-blue.svg)
![MIT License](https://img.shields.io/badge/license-MIT-green.svg)

![Screenshot from 2024-02-27 18-27-12](https://github.com/s5y-ux/CanvasAutoGrader/assets/59636597/ce7262fd-5f52-4d7c-8315-07785626ffac)


## Video Demo
![IMAGE ALT TEXT HERE](https://www.youtube.com/watch?v=8viAI7NGBGY)

Welcome to CanvasAutoGrader, an innovative tool designed to automate the grading process for assignments submitted through Canvas LMS (Learning Management System). By leveraging unit testing frameworks alongside the Canvas API, CanvasAutoGrader streamlines the assessment of student submissions, ensuring accurate, fair, and timely grading.

## Features

- **Automatic Grading**: Automatically evaluates and grades assignments based on predefined unit tests.
- **Canvas API Integration**: Seamlessly fetches assignments from Canvas, posts grades, and provides feedback directly within the LMS.
- **Customizable Test Cases**: Allows educators to define custom test cases for each assignment, ensuring flexibility and adaptability to various teaching methodologies.
- **Feedback Generation**: Generates detailed feedback for each submission, helping students understand their mistakes and learn from them.
- **Batch Processing**: Efficiently processes multiple submissions simultaneously, saving time and reducing manual effort.
- **Secure and Reliable**: Implements best practices to ensure the security of student data and the reliability of the grading process.

## Getting Started

### Prerequisites

- A Canvas LMS account with API access enabled.
- Python 3.6 or higher.
- Installation of required Python libraries: `requests`, `unittest`.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CanvasAutoGrader.git
   ```

2. Navigate to the CanvasAutoGrader directory:
   ```bash
   cd CanvasAutoGrader
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Rename `config.sample.json` to `config.json`.
2. Edit `config.json` to include your Canvas API key, course ID, and other relevant settings.

### Writing Unit Tests

- Refer to the `examples` directory for sample unit tests.
- Create a new Python file for your assignment's unit tests in the `tests` directory.
- Use Python's `unittest` framework to define test cases for the assignment.

### Running CanvasAutoGrader

To execute CanvasAutoGrader and grade assignments:

```bash
python autograder.py
```

## Usage Examples

For detailed examples, including how to write unit tests and configure the tool for your courses, please see the `docs` folder.

## Contributing

We welcome contributions from the community! If you're interested in improving CanvasAutoGrader, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

---

CanvasAutoGrader is not affiliated with or endorsed by Canvas LMS or Instructure. All trademarks belong to their respective owners.
