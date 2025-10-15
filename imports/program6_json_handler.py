"""
Program 6: JSON Data Manager
Practice: import json and working with JSON data
This program demonstrates JSON handling for data persistence and API interactions.
"""

import json
from json import JSONEncoder, JSONDecoder
from datetime import datetime, date
from typing import Dict, List, Any
import os

# Custom JSON Encoder for handling special types
class CustomJSONEncoder(JSONEncoder):
    """Custom JSON encoder to handle datetime objects"""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

class StudentDatabase:
    """A simple student database using JSON for storage"""

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_data()

    def load_data(self):
        """Load students from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.students = json.load(f)
                print(f"Loaded {len(self.students)} students from {self.filename}")
            except json.JSONDecodeError as e:
                print(f"Error loading JSON: {e}")
                self.students = []
        else:
            print(f"No existing database found. Starting fresh.")
            self.students = []

    def save_data(self):
        """Save students to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.students, f, indent=4, cls=CustomJSONEncoder)
            print(f"Saved {len(self.students)} students to {self.filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_student(self, student: Dict):
        """Add a new student"""
        student['id'] = len(self.students) + 1
        student['created_at'] = datetime.now().isoformat()
        self.students.append(student)
        self.save_data()
        return student

    def get_all_students(self) -> List[Dict]:
        """Get all students"""
        return self.students

    def find_student(self, student_id: int) -> Dict:
        """Find a student by ID"""
        for student in self.students:
            if student.get('id') == student_id:
                return student
        return None

    def update_student(self, student_id: int, updates: Dict) -> bool:
        """Update a student's information"""
        for i, student in enumerate(self.students):
            if student.get('id') == student_id:
                self.students[i].update(updates)
                self.students[i]['updated_at'] = datetime.now().isoformat()
                self.save_data()
                return True
        return False

    def delete_student(self, student_id: int) -> bool:
        """Delete a student"""
        for i, student in enumerate(self.students):
            if student.get('id') == student_id:
                del self.students[i]
                self.save_data()
                return True
        return False

def json_string_operations():
    """Demonstrate JSON string operations"""
    print("=== JSON String Operations ===\n")

    # Python object to JSON string
    data = {
        "name": "John Doe",
        "age": 25,
        "grades": [85, 90, 78],
        "is_enrolled": True,
        "address": {
            "street": "123 Main St",
            "city": "Boston",
            "zip": "02134"
        }
    }

    # Convert to JSON string
    json_string = json.dumps(data, indent=2)
    print("Python Dict to JSON String:")
    print(json_string)

    # Parse JSON string back to Python object
    parsed_data = json.loads(json_string)
    print(f"\nParsed back - Name: {parsed_data['name']}, Age: {parsed_data['age']}")

    # Compact JSON (no indentation)
    compact_json = json.dumps(data, separators=(',', ':'))
    print(f"\nCompact JSON (length: {len(compact_json)} chars):")
    print(compact_json[:50] + "...")

def json_file_operations():
    """Demonstrate JSON file operations"""
    print("\n=== JSON File Operations ===\n")

    # Sample data
    config_data = {
        "app_name": "Student Manager",
        "version": "1.0.0",
        "settings": {
            "theme": "dark",
            "language": "en",
            "auto_save": True,
            "max_records": 1000
        },
        "features": ["search", "export", "import", "backup"],
        "last_updated": datetime.now().isoformat()
    }

    # Write to file
    config_file = "config.json"
    with open(config_file, 'w') as f:
        json.dump(config_data, f, indent=4)
    print(f"Configuration saved to {config_file}")

    # Read from file
    with open(config_file, 'r') as f:
        loaded_config = json.load(f)

    print(f"Loaded configuration:")
    print(f"  App: {loaded_config['app_name']} v{loaded_config['version']}")
    print(f"  Theme: {loaded_config['settings']['theme']}")
    print(f"  Features: {', '.join(loaded_config['features'])}")

    # Clean up
    if os.path.exists(config_file):
        os.remove(config_file)
        print(f"\nCleaned up: Removed {config_file}")

def nested_json_handling():
    """Demonstrate handling of nested JSON structures"""
    print("\n=== Nested JSON Handling ===\n")

    # Complex nested structure
    company_data = {
        "company": "Tech Corp",
        "employees": [
            {
                "id": 1,
                "name": "Alice Johnson",
                "department": "Engineering",
                "skills": ["Python", "JavaScript", "SQL"],
                "projects": [
                    {"name": "Project A", "status": "completed"},
                    {"name": "Project B", "status": "in_progress"}
                ]
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "department": "Marketing",
                "skills": ["SEO", "Content Writing"],
                "projects": [
                    {"name": "Campaign X", "status": "planning"}
                ]
            }
        ],
        "metadata": {
            "total_employees": 2,
            "departments": ["Engineering", "Marketing"],
            "created_date": datetime.now().isoformat()
        }
    }

    # Pretty print with custom encoder
    json_output = json.dumps(company_data, indent=2, cls=CustomJSONEncoder)
    print("Complex Nested Structure:")
    print(json_output[:300] + "...\n")  # Show first 300 chars

    # Access nested data
    print("Accessing Nested Data:")
    for employee in company_data["employees"]:
        print(f"\nEmployee: {employee['name']}")
        print(f"  Department: {employee['department']}")
        print(f"  Skills: {', '.join(employee['skills'])}")
        print(f"  Active Projects: {len([p for p in employee['projects'] if p['status'] != 'completed'])}")

def demonstrate_student_database():
    """Demonstrate the student database system"""
    print("\n=== Student Database Demo ===\n")

    # Create database instance
    db = StudentDatabase("demo_students.json")

    # Add students
    students_to_add = [
        {"name": "Emma Wilson", "age": 20, "major": "Computer Science", "gpa": 3.8},
        {"name": "Michael Brown", "age": 22, "major": "Mathematics", "gpa": 3.6},
        {"name": "Sarah Davis", "age": 21, "major": "Physics", "gpa": 3.9}
    ]

    print("Adding students to database...")
    for student_data in students_to_add:
        student = db.add_student(student_data)
        print(f"  Added: {student['name']} (ID: {student['id']})")

    # Display all students
    print("\nAll Students in Database:")
    all_students = db.get_all_students()
    for student in all_students:
        print(f"  ID: {student['id']}, Name: {student['name']}, Major: {student['major']}, GPA: {student['gpa']}")

    # Update a student
    if len(all_students) > 0:
        first_student_id = all_students[0]['id']
        db.update_student(first_student_id, {"gpa": 3.95})
        print(f"\nUpdated student ID {first_student_id}'s GPA to 3.95")

    # Find a specific student
    if len(all_students) > 1:
        second_student = db.find_student(all_students[1]['id'])
        if second_student:
            print(f"\nFound student: {json.dumps(second_student, indent=2, cls=CustomJSONEncoder)}")

    # Clean up
    if os.path.exists("demo_students.json"):
        os.remove("demo_students.json")
        print("\nCleaned up: Removed demo_students.json")

def json_validation_example():
    """Demonstrate JSON validation and error handling"""
    print("\n=== JSON Validation & Error Handling ===\n")

    # Valid JSON
    valid_json = '{"name": "Test", "value": 123}'
    try:
        data = json.loads(valid_json)
        print(f"Valid JSON parsed successfully: {data}")
    except json.JSONDecodeError as e:
        print(f"Error: {e}")

    # Invalid JSON examples
    invalid_jsons = [
        '{"name": "Test" "value": 123}',  # Missing comma
        "{'name': 'Test'}",  # Single quotes
        '{"name": "Test",}',  # Trailing comma
    ]

    print("\nTesting invalid JSON strings:")
    for i, invalid_json in enumerate(invalid_jsons, 1):
        try:
            data = json.loads(invalid_json)
            print(f"  {i}. Parsed successfully (unexpected)")
        except json.JSONDecodeError as e:
            print(f"  {i}. Invalid JSON detected: {e.msg}")

def main():
    """Main function to run all JSON demonstrations"""
    print("=" * 60)
    print("JSON DATA HANDLING DEMONSTRATION")
    print("=" * 60)

    # Run all demonstrations
    json_string_operations()
    json_file_operations()
    nested_json_handling()
    demonstrate_student_database()
    json_validation_example()

    print("\n" + "=" * 60)
    print("JSON demonstration completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()