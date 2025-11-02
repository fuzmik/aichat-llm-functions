# @describe Lints a Python file using pylint.
# @param file_path! The path to the Python file to lint.
def run(file_path: str):
    """
    Lints a Python file using pylint.

    Args:
        file_path: The absolute or relative path to the Python file to lint.
    """
    import subprocess
    import sys

    try:
        # Construct the pylint command
        # We use sys.executable to ensure we use the same Python interpreter
        # that is running this script, which should have pylint installed.
        command = [sys.executable, "-m", "pylint", file_path]

        # Execute the command
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False # Do not raise an exception if pylint returns a non-zero exit code
        )

        # Return the output
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
    except FileNotFoundError:
        return {
            "stdout": "",
            "stderr": "Error: pylint command not found. Please ensure pylint is installed and in your PATH.",
            "exit_code": 1
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"An unexpected error occurred: {e}",
            "exit_code": 1
        }
