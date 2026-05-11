class circle():

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def circle_area(self):
        return self.length*self.width
    
length = int(input("Enter a length : "))
width = int(input("Enter a width: "))
newcircle = (length, width)
print("The area of the circle is : ", newcircle.circle_area)