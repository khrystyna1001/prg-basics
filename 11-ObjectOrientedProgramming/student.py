# class definition
class Student():
    def __init__(self, number):
        self.name = ""
        self.age = 0
        self.number = number

def main():
    # object creation based on the class
    student1 = Student(236523)
    student2 = Student(236524)
    student3 = Student(236525)
    student1.name = "Dominic"
    student1.age = 19
    student2.name = "Olivia"
    student2.age = 21
    student3.name = 'Mark'
    student3.age = 18

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.number}')
    print(f'{student2.name}, {student2.age} years old, {student2.number}')
    print(f'{student3.name}, {student3.age} years old, {student3.number}')

if __name__ == "__main__":
    main()