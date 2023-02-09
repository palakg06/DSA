class Employee:
    
    def __init__(self,fn,ln,id,des):
        self.fname=fn
        self.lname=ln
        self.empID=id
        self.designation=des
    def getname(self):
        return self.fname+" "+ self.lname
    def getemail(self):
        return self.fname+'.'+self.lname+'@psit.in'
    def getdesignation(self):
       return self.designation
    def getempid(self):
       return self.empID
emp1=Employee("Pawan","Kumar",1200,'student')
emp2=Employee("manoj","Shukla",1300,'teacher')
emp3=Employee("Paddu","yadav",1400,'manager')
print(emp2.getemail())
print(emp1.getdesignation())
print(emp3.getempid())
print(emp2.getname())
