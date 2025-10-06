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


s1 = Student(101, "Vaishnavi", 20, 88.5)
s1.display()

print("\nUsing __str__ method:")
print(s1)

print("\nAccepting new student data:")
s2 = Student(0, "", 0, 0)
s2.accept()
s2.display()