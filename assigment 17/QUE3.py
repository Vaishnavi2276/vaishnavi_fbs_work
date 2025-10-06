class Student:
    
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    
    def accept(self):
        self.StudentId = input("Enter Student ID: ")
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    
    def display(self):
        print(f"Student ID     : {self.StudentId}")
        print(f"Name           : {self.Name}")
        print(f"Age            : {self.Age}")
        print(f"Percentage     : {self.Percentage}")
        print(f"Rank           : {self.calculateRank()}")

    def calculateRank(self):
        if self.Percentage >= 90:
            return "A+"
        elif self.Percentage >= 75:
            return "A"
        elif self.Percentage >= 60:
            return "B"
        elif self.Percentage >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return (f"Student[ID={self.StudentId}, Name={self.Name}, "
                f"Age={self.Age}, Percentage={self.Percentage}, "
                f"Rank={self.calculateRank()}]")

class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_of_internship

    def accept(self):
        super().accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks of Internship: "))

    def display(self):
        super().display()
        print(f"Specialization : {self.Specialization}")
        print(f"Internship Marks : {self.MarksOfInternship}")

    
    def calculateRank(self):
        final_score = (self.Percentage * 0.7) + (self.MarksOfInternship * 0.3)
        if final_score >= 90:
            return "A+"
        elif final_score >= 75:
            return "A"
        elif final_score >= 60:
            return "B"
        elif final_score >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return (f"MedicalStudent[ID={self.StudentId}, Name={self.Name}, "
                f"Age={self.Age}, Percentage={self.Percentage}, "
                f"Specialization={self.Specialization}, "
                f"InternshipMarks={self.MarksOfInternship}, "
                f"Rank={self.calculateRank()}]")

print("=== Base Class Student ===")
s1 = Student(101, "Vaishnavi", 20, 85)
s1.display()
print(s1)

print("\n=== Derived Class MedicalStudent ===")
m1 = MedicalStudent(301, "Riya", 22, 80, "Cardiology", 90)
m1.display()
print(m1)

print("\n=== Accepting New Medical Student Data ===")
m2 = MedicalStudent(0, "", 0, 0, "", 0)
m2.accept()
m2.display()
