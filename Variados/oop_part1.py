# learning python - cap 26
class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)
#------
x = FirstClass()
y = FirstClass()
#------
x.setdata("King Arthur")
y.setdata(3.14159)
#------
x.display()
y.display()
#------
x.data = "New Value"
x.display()
#------
x.anothername = "spam"
x.display()
#------
z = SecondClass()
z.setdata(42)
z.display()
