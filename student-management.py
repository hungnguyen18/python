class Student:
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender


class StudentManager:
    def __init__(self):
        self.students = []

    def list_students(self):
        for student in self.students:
            print(f"id: {student.id} - name: {student.name} - gender: {student.gender}")

    def add_students(self, id, name, gender):
        student = Student(id, name, gender)
        self.students.append(student)

    def remove_students(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                return True
        return False

    def update_students(self, id, name, gender):
        for student in self.students:
            if student.id == id:
                student.name = name
                student.gender = gender
                return True
        return False


def main():
    student_manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. List Students")
        print("5. Quit")
        choice = int(input("Choose: "))

        if choice == 1:
            print("add student")
            id = str(input("\nid: "))
            name = str(input("name: "))
            gender = str(input("gender: "))
            student_manager.add_students(id, name, gender)
        elif choice == 2:
            print("remove student")
            id = str(input("\nid: "))
            if student_manager.remove_students(id):
                print("remove student successfully")
            else:
                print("remove student failed")
        elif choice == 3:
            print("update student")
            id = str(input("\nid: "))
            name = str(input("new name: "))
            gender = str(input("new gender: "))
            if student_manager.update_students(id, name, gender):
                print("Updated student successfully")
            else:
                print("Couldn't update student")
        elif choice == 4:
            print("List of students")
            student_manager.list_students()
        elif choice == 5:
            break
        else:
            print("No choice")


main()
