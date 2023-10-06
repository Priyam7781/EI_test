class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}
        self.students = {}

    def add_classroom(self, class_name):
        if class_name not in self.classrooms:
            self.classrooms[class_name] = []
            print(f"Classroom '{class_name}' has been created.")
        else:
            print(f"Classroom '{class_name}' already exists.")

    def add_student(self, student_id, class_name):
        if class_name in self.classrooms:
            if student_id not in self.students:
                self.students[student_id] = class_name
                self.classrooms[class_name].append(student_id)
                print(f"Student '{student_id}' has been enrolled in '{class_name}'.")
            else:
                print(f"Student '{student_id}' is already enrolled in a class.")
        else:
            print(f"Classroom '{class_name}' does not exist.")

    def schedule_assignment(self, class_name, assignment_details):
        if class_name in self.classrooms:
            print(f"Assignment for '{class_name}' has been scheduled. Details: {assignment_details}")
        else:
            print(f"Classroom '{class_name}' does not exist.")

    def submit_assignment(self, student_id, class_name, assignment_details):
        if student_id in self.students and self.students[student_id] == class_name:
            print(f"Assignment submitted by Student '{student_id}' in '{class_name}'. Details: {assignment_details}")
        else:
            print(f"Invalid submission: Student '{student_id}' is not enrolled in '{class_name}'.")

# Example Usage:
manager = VirtualClassroomManager()

# Adding a classroom
manager.add_classroom("Math101")

# Enrolling a student
manager.add_student("123", "Math101")

# Scheduling an assignment
manager.schedule_assignment("Math101", "Problem Set 1")

# Submitting an assignment
manager.submit_assignment("123", "Math101", "Solution to Problem Set 1")
