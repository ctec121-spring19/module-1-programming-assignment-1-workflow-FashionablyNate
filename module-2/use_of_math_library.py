# Nathan Spelts
# Code for various formulas

# number one
def main():
    print()

    print("This program calculates the volume of a sphere.")
    pi = 3.14159265359

    radius1 = eval(input("Enter the radius: "))
    volume = 4/3 * pi * radius1 * radius1 * radius1

    print("The volume of your sphere is:", volume)

    print()
# number two
    print("This program calculates the area of a circle.")

    radius2 = eval(input("Enter the radius: "))
    area1 = 4 * pi * radius2 * radius2

    print("The area of your circle is:", area1)

    print()
# number three
    print("This program calculates the slope of a line.")

    x1, y1, x2, y2 = eval(input("Enter your coordinates seperated by commas like so x1, y1, x2, y2: "))
    slope = (y2 - y1)/(x2 - x1)

    print("The slope of your line is:", slope)

    print()
# number four
    print("This program calculates the semiperimeter of a triangle.")

    a, b, c = eval(input("Enter the angles of your triangle seperated by commas: "))
    s = (a + b + c)/2

    print("The semiperimeter of your triangle is:", s)

    print()
# number five
    print("This program calculates the area of a triangle.")

    a1, b1, c1 = eval(input("Enter the lengths of the sides of your triangle seperated by commas: "))
    area2 = (s * (s - a) * (s - b) * (s - c))** 0.5

    print("The area of your triangle is:", area2)

    print()

    print("Final Results:")
    print("volume of your sphere:", volume)
    print("area of your circle:", area1)
    print("slope of your line:", slope)
    print("semiperimeter of your triangle:", s)
    print("area of your triangle:", area2)
    print()
    print("Have a nice day!")
    print()
main()
