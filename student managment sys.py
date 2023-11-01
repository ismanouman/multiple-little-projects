#Student Management System

# Design a Student Management System that allows managing 
# student records, including their personal information, courses, and grades. 
# Implement the following classes:

# 1. *Person*:
#    - Attributes: name (string), age (integer)
#    - Methods:
#      - `display_details()`: Display the name and age of the person.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
    

# 2. *Student* (subclass of Person):
#    - Additional Attributes: roll_number (string), courses (list of strings), grades (dictionary)
#    - Methods:
#      - `add_course(course: string)`: Add a course to the student's course list.
#      - `update_grade(course: string, grade: string)`: Update the grade for a specific course.
#      - `display_details()`: Display the name, age, roll number, courses, and grades of the student.
class student(person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number=roll_number
        self.courses=[]
        self.grades={}
    def add_course(self,course):
         self.courses.append(course)
        
    def update_grade(self,course,grade):
         self.grades[course]=grade
    def display_details(self):
        super().display_details()
        print("roll_number:",self.roll_number)
        
        for course in self.courses:
            print(course)
        print('Grades')
        for course ,grade in self.grades.items():
             print(f'{course}:{grade}')

# 3. *Teacher* (subclass of Person):
#    - Additional Attributes: employee_id (string), courses (list of strings)
#    - Methods:
#      - `add_course(course: string)`: Add a course that the teacher teaches.
#      - `display_details()`: Display the name, age, employee ID, and courses taught by the teacher.

class teacher(person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.courses=[]
    def add_course(self,courses):
        self.courses.append(courses)
    def display_details(self):
       
        super().display_details()
        print("employee_ID :",self.employee_id)
        for course in self.courses:
            print(course)
       

# Write a Python program that demonstrates the functionality of the Student Management System by performing the following actions:

# 1. Create three instances of students with the following details:
#    - Student 1: Name: John Doe, Age: 20, Roll Number: S001
#    - Student 2: Name: Alice Smith, Age: 19, Roll Number: S002
#    - Student 3: Name: Bob Johnson, Age: 21, Roll Number: S003

student1=student("John Doe","20","s001")
student2=student("Alice Smith","19","s002")
student3=student("Bob johnson","21","s003")

# 2. Create an instance of a teacher with the following details:
#    - Teacher: Name: Mr. Smith, Age: 35, Employee ID: T001
teacher=teacher("Mr.Smith","35","T001")

# Add the following courses for the teacher:
#    - Course 1: Mathematics
#    - Course 2: English
teacher.add_course("course 1:Mathematics")
teacher.add_course("course 2:English")

# 4. Add the following courses for each student:
#    - Student 1: Course 1: Mathematics, Course 2: Physics
#    - Student 2: Course 1: English
#    - Student 3: Course 1: Mathematics, Course 2: Chemistry

student1.add_course("Course 1: Mathematics")
student1.add_course("course 2:Physics")
student2.add_course("course 1:English")
student3.add_course("course 1:Mathematics")
student3.add_course("course 2:Chemistry")

# 5. Update the grades for the students as follows:
#    - Student 1: Mathematics: A, Physics: B+
#    - Student 3: Mathematics: A-, Chemistry: B
student1.update_grade("Mathematics"," A")
student1.update_grade("Physics", "B+")
student3.update_grade("Mathematics", "A-")
student3.update_grade("Chemistry" ,"B")

# 6. Display the details of each student and the teacher by calling the `display_details()` 
# method for each instance.
print("__student_1__")
student1.display_details()
print("__student_2__")
student2.display_details()
print("__student_3__")
student3.display_details()
print("__teacher_details__")
teacher.display_details()