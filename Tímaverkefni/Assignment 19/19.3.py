def get_float_list(grades):
    return [float(i) for i in grades]

class Student:

    def __init__(self, ID, grades):
        self.student_ID = int(ID)
        self.grades = get_float_list(grades)

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.student_ID, self.grades)

    def __lt__(self, other):
        return self.get_average() < other.get_average()

    def get_average(self):
        return sum(self.grades)/len(self.grades)

def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if (john < alice):
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")

main()