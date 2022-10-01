#Task_2
class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def firstname(self):
        return self.fname.title()
    def lastname(self):
        return self.lname.title()
    def full_name(self):
        return self.fname.title() + " " + self.lname.title()
    def initials(self):
        initials = str(self.fname[0]) + "." + str(self.lname[0])
        return initials
obj1 = Name('Malika', 'BERIKOVA')
print(obj1.firstname())
print(obj1.lastname())
print(obj1.full_name())
print(obj1.initials())
obj2 = Name('ARAILYM', 'Tleubayeva')
print(obj2.firstname())
print(obj2.lastname())
print(obj2.full_name())
print(obj2.initials())