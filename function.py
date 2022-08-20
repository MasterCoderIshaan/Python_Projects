import string


def circle():
    r = float(input("Enter radius for your circle : "))
    area = 22/7*r*r
    print(area , "unit^2")

def triangle():
    b = float(input("Enter base of Traingle : "))
    h = float(input("Enter height of Triangle : "))
    area = 1/2 * b * h
    print(area , "unit^2")


def square ():
    s = float(input("Enter side of square : "))
    area=s*4
    print(area,"unit^2")

def trapizium ():
    t = float(input("Enter first parellel side : "))
    t2 = float(input("Enter second parellel side : "))
    h = float(input("Enter height of tarpizium : "))
    area=1/2*(t+t2)*h
    print(area,"unit^2")

def parellelogram():
    b = float(input("Enter base of the parellelogram : "))
    h = float(input("Enter height of parellelogram : "))
    area = b*h
    print(area, "unit^2")

r = input("Area of circle , triangle , parellelogram , trapizium : ")

if(r=="circle"):
    circle()

elif(r=="square"):
    square()

elif(r=="trapizium"):
    trapizium()

elif(r=="parellelogram"):
    parellelogram()

else:
    triangle()