# Nathan Spelts
# Code for various formulas

# number one
def main():
    print()

    print("This program calculates the volume of a sphere.")
    pi = 3.14159265359

    print()

    radius1 = eval(input("Enter the radius: "))
    volume = 4/3 * pi * radius1 * radius1 * radius1

    print()

    print("The volume is:", volume)

    print()
# number two
    print("This program calculates the area of a circle.")

    print()

    radius2 = eval(input("Enter the radius: "))
    area1 = 4 * pi * radius2 * radius2

    print()

    print("The area is:", area1)

    print()
# number three
    print("This program calculates the slope of a line.")

    print()

    x1, y1, x2, y2 = eval(input("Enter your coordinates seperated by commas like so x1, y1, x2, y2: "))
    slope = (y2 - y1)/(x2 - x1)

    print()

    print("The slope of the line is:", slope)

    print()
# number four
    print("This program calculates the semiperimeter of a triangle.")

    print()

    a, b, c = eval(input("Enter the angles of your triangle seperated by commas: "))
    s = (a + b + c)/2

    print()

    print("The semiperimeter of your triangle is:", s)

    print()
# number five
    print("This program calculates the area of a triangle.")
    
    print()

    a1, b1, c1 = eval(input("Enter the lengths of the sides of your triangle seperated by commas: "))
    area2 = (s * (s - a) * (s - b) * (s - c))** 0.5

    print()

    print("The area of your triangle is:", area2)

    print()
main()
