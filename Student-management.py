class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {}

    def get_marks(self):
        return self.__marks


    def add_marks(self,subject,marks):
        self.__marks[subject] = marks

    def calculate_average(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        average = total/len(self.__marks)
        return average


    def is_passed(self):
        has_passed = all(mark >= 35 for mark in self.__marks.values())
        if has_passed:
            print(f'{self.name} has passed')
        else:
            print(f"{self.name} has failed")

    def calculate_grade(self):
        
        percentage = self.calculate_average()

        print('Grade: ', end="")

        if percentage >= 90:
            print('A+') 
        elif percentage >= 80:
            print("A")
        elif percentage >= 75:
            print('B+')
        elif percentage >=70:
            print('B')
        else:
            print("C")


class ReportCard:
    @staticmethod
    def generate(student: Student):
        student_marks = student.get_marks()

        print(f"\nName: {student.name}\tRoll No. {student.roll_no}")
        print("----Marks----")

        for subject, marks in student_marks.items():
            print(f"{subject} - {marks}")

        # These statements must be OUTSIDE the for loop
        print("-------------")
        print(f"Average: {student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()
        print()

students = {}

while True:
    print('\n---Student Management System---')
    print('1.Add Student')
    print('2.Add Marks')
    print('3.Display All Students')
    print('4.Generate Report Card')
    print('5.Exit')

    choice = input('Enter Your choice: ')

    if choice=='1':
        name = input('enter your name: ')
        roll_no = int(input('enter your roll no: '))

        new_student=Student(name,roll_no)
       
        students[roll_no]=new_student
        print('Student addend Successfully')

    elif choice == '2':
        roll_no = int(input("Enter roll number: "))

        if roll_no in students:
            student = students[roll_no]

            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))

            student.add_marks(subject, marks)

            print("Marks added successfully!")

        else:
            print("Student not found!")

    elif choice == '3':
        for roll_no , student in students.items():
            print(f'Name: {student.name}')
            print(f'Roll No: {student.roll_no}')

    elif choice == '4':
        roll_no = int(input('enter your roll number: '))

        if roll_no in students:
            student = students[roll_no]
            ReportCard.generate(student)
        else:
            print('Student not found')


    elif choice == '5':
        print('Exiting Student Management system...')
        break


            
    



       