class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
y.setdata(3.13159)

x.display()
y.display()

x.data = "New value"
x.display()

x.anothername = "spam"
#------------
class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

z = SecondClass()
z.setdata(42)
z.display()
#------------
