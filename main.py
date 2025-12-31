class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40

    def __str__(self):
        return (
            f"Student ID    : {self.id}\n"
            f"Student Name  : {self.name}\n"
            f"Student Marks : {self.marks}"
        )


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("\nNo students available.\n")
            return

        for student in self.students:
            print(student)
            print("Result :", "Pass" if student.is_pass() else "Fail")
            print("-" * 30)

    def save_to_file(self):
        with open("Students.txt", "w") as fs:
            for student in self.students:
                fs.write(f"{student.id},{student.name},{student.marks}\n")
        print("\nStudents saved successfully.\n")

    def load_from_file(self):
        try:
            with open("Students.txt", "r") as fs:
                for line in fs:
                    id, name, marks = line.strip().split(",")
                    self.students.append(Student(int(id), name, int(marks)))
        except FileNotFoundError:
            pass   # No file exists on first run


# -------- MAIN PROGRAM --------

def main():
    manager = StudentManager()
    manager.load_from_file()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Students")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))

                student = Student(id, name, marks)
                manager.add_student(student)
                print("Student added successfully.")

            except ValueError:
                print("Invalid input. ID and Marks must be numbers.")

        elif choice == 2:
            manager.display_students()

        elif choice == 3:
            manager.save_to_file()

        elif choice == 4:
            manager.save_to_file()
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# Program starts here
main()
