class Student:
    def __init__(self, No, N, ict_marks, Et_marks, Bt_marks):
        self.index = No
        self.Name = N
        self.ICT = ict_marks
        self.ET = Et_marks
        self.BT = Bt_marks

    def Tot(self):
        a = (self.BT+self.ET+self.ICT)
        return a

    def Average(self):
        a = self.Tot()/3
        return a

    def Show(self):
        print("\n"+'-'*45)
        print(" * Studet Index : ", self.index)
        print(" * Studet Name : ", self.Name)
        print(" * Studet ICT Marks : ", self.ICT)
        print(" * Studet Etech Marks : ", self.ET)
        print(" * Studet Btech Marks : ", self.BT)
        print("\n * Studet Total : ", self.Tot())
        print(" * Studet Average : ", self.Average())
        print('-'*45+'\n')


All = []
Count = 1
while True:
    print("\n\t\t- This is Student Number", Count, '-')
    Index = input("Enter Index No : ")
    Name = input("Enter Name : ")
    it = int(input("Enter Ict Marks : "))
    bt = int(input("Enter Btech Marks : "))
    et = int(input("Enter Etech Marks : "))

    our_student = Student(Index, Name, it, et, bt)
    All.append(our_student)
    
    breaking = input("\n Enter x to Finesh : ")
    if breaking == 'x':
        break
    Count+=1


for i in All:
    i.Show()

input()