import sys
import time
import math
import colored
from colored import stylize

answer = colored.fg(1) + colored.attr("bold")

print("""1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, 
Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 

Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
""")

print(stylize("=== Answer ===", answer))

print("""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
""")

print("""
2. Write a Python program to get the Python version you are using.
""")

print(stylize("=== Answer ===", answer))

print(sys.version)
print(sys.version_info)

print("""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
""")

print(stylize("=== Answer ===", answer))

print("Current date and time :")
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print("""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
""")

print(stylize("=== Answer ===", answer))

radius = float(input("Please enter radius: "))
radius **= 2
print("The area of the circle is:", math.pi * radius)

print("""
5. Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them. 
""")

print(stylize("=== Answer ===", answer))

fname = input("First name: ")
lname = input("Last name: ")