class Emp:
    def __init__(self,id,name,sal,dep):
        self.eid=id
        self.ename=name
        self.sal= sal
        self.dep= dep
    def __str__(self):
        return f"{self.eid}, {self.ename}, {self.sal}, {self.dep}"
    
e1 = Emp(102,"vaishu",50000,"teaching")
print(e1)
