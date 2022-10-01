#Task_1
class First:
    color = 'red'
    def out(self):
        print(self.color + "!")
class Second:
    color = 'red'
    form = 'circle'
    area = 1
    def changecolor(self, newcolor):
        self.color = newcolor
    def changeform(self, newform):
        self.form = newform
    def changearea(self, newarea):
        self.area = newarea
obj1 = Second()
obj2 = Second()
obj3 = Second()
print("Object 1 (default): ", obj1.color, obj1.form, obj1.area)
print("Object 2 (default): ", obj2.color, obj2.form, obj2.area)
print("Object 3 (default): ", obj3.color, obj3.form, obj3.area)
obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changearea(16)
obj2.changeform("oval")
obj3.changecolor("brown")
obj3.changearea(10)
obj3.changeform("triangle")
print("Object 1 (result): ", obj1.color, obj1.form, obj1.area)
print("Object 2 (result): ", obj2.color, obj2.form, obj2.area)
print("Object 3 (result): ", obj3.color, obj3.form, obj3.area)



