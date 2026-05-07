class rectangle():

    def __init__(self, l, w):
        self.length = l
        self.width = w


    def rectangle_area(self):
        return self.length*self.width
    
length = int(input("Enter a Length"))
width = int(input("Enter a width"))
newrectangle = rectangle(length, width)
print("Area of rectangle : ", newrectangle.rectangle_area())