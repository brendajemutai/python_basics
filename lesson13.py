#cylinder-->class
class Cylinder:
    def __init__(self,radius,height,color):
        self.r=radius
        self.h=height
        self.rangi=color

#functions for manipulation
    def cal_area(self,is_closed=True):
        if is_closed==True:
            area=2 * 22/7 * self.r**2 + 2 * 22/7* self.r * self.h
            print(f"Area of closed cylinder is : {area}")
        else:
            area=22/7 * self.r**2 + 2 * 22/7* self.r * self.h
            print(f"Area of open cylinder is : {area}")

    def calc_volume(self):
        v=22/7 * self.r**2 * self.h
        print(f"Volume of cylinder is : {v}")

#object created from a class(cylinder)
c1=Cylinder(7,9,"Red")
c2=Cylinder(6.8,90,"Yellow")
c1.cal_area(is_closed=False)
c1.calc_volume()

