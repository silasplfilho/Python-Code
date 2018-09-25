class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        part1 = (self.coor2[0] - self.coor1[0])**2
        part2 = (self.coor2[1] - self.coor1[1])**2
        d = (part1 + part2)**(.5)
        return d

    def slope(self):
        part1 = (self.coor2[1] - self.coor1[1])
        part2 = (self.coor2[0] - self.coor1[0])
        m = part1 / part2
        return m
#
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()

#-----
class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v = (Cylinder.pi * (self.radius**2)) * self.height
        return v

    def surface_area(self):
        sa = (2 * (Cylinder.pi * (self.radius**2))) + ( 2 * Cylinder.pi * self.radius * self.height)
        return sa
#
c = Cylinder(2,3)
c.volume()
c.surface_area()
