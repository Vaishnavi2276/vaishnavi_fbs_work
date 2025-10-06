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



class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    
    def accept(self):
        super().accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def display(self):
        super().display()
        print(f"Branch         : {self.Branch}")
        print(f"Internal Marks : {self.InternalMarks}")


    def calculateRank(self):
        
        final_score = (self.Percentage * 0.8) + (self.InternalMarks * 0.2)
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
        return (f"EnggStudent[ID={self.StudentId}, Name={self.Name}, Age={self.Age}, "
                f"Percentage={self.Percentage}, InternalMarks={self.InternalMarks}, "
                f"Branch={self.Branch}, Rank={self.calculateRank()}]")
print("=== Base Class Student ===")
s1 = Student(101, "Vaishnavi", 20, 88.5)
s1.display()
print(s1)

print("\n=== Derived Class EnggStudent ===")
e1 = EnggStudent(201, "sauranh", 21, 82.5, "Computer", 85)
e1.display()
print(e1)

print("\n=== Accepting New Engineering Student Data ===")
e2 = EnggStudent(0, "", 0, 0, "", 0)
e2.accept()
e2.display()