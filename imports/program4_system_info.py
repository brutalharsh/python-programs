"""
Program 4: System Information Tool
Practice: import os, import sys, and import platform
This program demonstrates system and file operations using os and sys modules.
"""

import os
import sys
import platform
from pathlib import Path  # Modern way to handle paths

def system_information():
    """Display comprehensive system information"""
    print("=== System Information ===")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine Type: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {sys.version}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Platform: {sys.platform}")

def environment_variables():
    """Display and manage environment variables"""
    print("\n=== Environment Variables ===")

    # Common environment variables
    common_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'PYTHONPATH']

    for var in common_vars:
        value = os.environ.get(var, 'Not Set')
        if var == 'PATH':
            # Display first 3 PATH entries for brevity
            paths = value.split(os.pathsep)[:3]
            print(f"{var}: {os.pathsep.join(paths)}... (showing first 3)")
        else:
            print(f"{var}: {value}")

    # Set a custom environment variable
    os.environ['MY_CUSTOM_VAR'] = 'Hello from Python!'
    print(f"\nCustom Variable Set: MY_CUSTOM_VAR = {os.environ.get('MY_CUSTOM_VAR')}")

def directory_operations():
    """Demonstrate directory operations"""
    print("\n=== Directory Operations ===")

    # Current working directory
    cwd = os.getcwd()
    print(f"Current Directory: {cwd}")

    # Create a test directory structure
    test_dir = "test_directory"
    sub_dir = os.path.join(test_dir, "subdirectory")

    try:
        # Create directories
        os.makedirs(sub_dir, exist_ok=True)
        print(f"Created directory structure: {sub_dir}")

        # List directory contents
        print(f"\nContents of current directory:")
        items = os.listdir('.')
        for item in items[:5]:  # Show first 5 items
            item_path = os.path.join('.', item)
            if os.path.isdir(item_path):
                print(f"  [DIR]  {item}")
            else:
                print(f"  [FILE] {item}")

        # Check if paths exist
        print(f"\nPath existence check:")
        print(f"  {test_dir} exists: {os.path.exists(test_dir)}")
        print(f"  {test_dir} is directory: {os.path.isdir(test_dir)}")

        # Get file/directory information
        stat_info = os.stat(test_dir)
        print(f"\nDirectory stats for {test_dir}:")
        print(f"  Size: {stat_info.st_size} bytes")
        print(f"  Last modified: {stat_info.st_mtime}")

        # Clean up - remove test directory
        os.rmdir(sub_dir)
        os.rmdir(test_dir)
        print(f"\nCleaned up: Removed {test_dir}")

    except Exception as e:
        print(f"Error during directory operations: {e}")

def file_path_operations():
    """Demonstrate file path operations"""
    print("\n=== File Path Operations ===")

    # Different path operations
    sample_path = "/home/user/documents/file.txt"
    print(f"Sample path: {sample_path}")
    print(f"  Directory: {os.path.dirname(sample_path)}")
    print(f"  Filename: {os.path.basename(sample_path)}")
    print(f"  Split: {os.path.split(sample_path)}")
    print(f"  Extension: {os.path.splitext(sample_path)[1]}")

    # Join paths (cross-platform)
    joined_path = os.path.join("home", "user", "documents", "file.txt")
    print(f"\nJoined path: {joined_path}")

    # Absolute vs Relative paths
    print(f"\nCurrent file location: {__file__ if '__file__' in globals() else 'Interactive mode'}")
    print(f"Absolute path of '.': {os.path.abspath('.')}")

def python_path_info():
    """Display Python path information"""
    print("\n=== Python Path Information ===")
    print(f"Python Executable: {sys.executable}")
    print(f"Python Path (first 3):")
    for path in sys.path[:3]:
        print(f"  - {path}")

    # Command line arguments
    print(f"\nCommand Line Arguments: {sys.argv}")

    # Platform information
    print(f"Byte Order: {sys.byteorder}")
    print(f"Max Integer Size: {sys.maxsize}")

def memory_and_recursion():
    """Display memory and recursion limits"""
    print("\n=== Memory and Limits ===")

    # Recursion limit
    print(f"Recursion Limit: {sys.getrecursionlimit()}")

    # Reference count (CPython specific)
    sample_list = [1, 2, 3]
    print(f"Reference count for sample_list: {sys.getrefcount(sample_list)}")

    # Size of objects
    print(f"\nSize of common objects (bytes):")
    print(f"  Integer (42): {sys.getsizeof(42)}")
    print(f"  String ('hello'): {sys.getsizeof('hello')}")
    print(f"  List ([1,2,3]): {sys.getsizeof([1, 2, 3])}")
    print(f"  Dictionary ({'a':1}): {sys.getsizeof({'a': 1})}")

def main():
    """Main function to run all demonstrations"""
    print("=" * 50)
    print("SYSTEM AND FILE OPERATIONS DEMO")
    print("=" * 50)

    # Run all demonstrations
    system_information()
    environment_variables()
    directory_operations()
    file_path_operations()
    python_path_info()
    memory_and_recursion()

    print("\n" + "=" * 50)
    print("Demo completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()