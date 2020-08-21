import sys
import time
import math
import calendar
import colored
from colored import stylize

answer = colored.fg(1) + colored.attr("bold")

# print("""1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high,
# Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
#
# Output :
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
# """)
#
# print(stylize("=== Answer ===", answer))
#
# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
# """)
#
# print("""
# 2. Write a Python program to get the Python version you are using.
# """)
#
# print(stylize("=== Answer ===", answer))
#
# print(sys.version)
# print(sys.version_info)
#
# print("""
# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# """)
#
# print(stylize("=== Answer ===", answer))
#
# print("Current date and time :")
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
#
# print("""
# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# """)
#
# print(stylize("=== Answer ===", answer))
#
# radius = float(input("Please enter radius: "))
# radius **= 2
# print("The area of the circle is:", math.pi * radius)
#
# print("""
# 5. Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.
# """)
#
# print(stylize("=== Answer ===", answer))
#
# fname = input("First name: ")
# lname = input("Last name: ")
#
# print(lname, fname)
#
# print("""
# Write a Python program which accepts a sequence of comma-separated numbers from user and
# generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
# """)
#
# print("""
# === Answer ===
# """)
# l = list()
#
# while True:
#     try:
#         seq = input("adf ")
#         if seq == "done":
#             break
#         else:
#             l.append(seq)
#     except:
#         print("Please enter a number")
#
#
# kk = "".join(l)
# kk = tuple(kk)
#
# print("list:", l)
# print(type(l))
# print("Tuple:", kk)
# print(type(kk))
#
# print("""
# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java""")
#
# print("""
# === Answer ===""")
#
# fname = input("filenmae: ")
# ext = fname.split(".")
# print(ext[-1])  # it must be -1 otherwise if a period is in the filename you won't output the extension
#
# print("""
# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]""")
#
# print("""
# === Answer ===""")
#
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])
#
# print("""
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014""")
#
# print("""
# === Answer ===""")
# exam_st_date = (11, 12, 2014)
# date = list()
# for x in exam_st_date:
#     x = str(x)
#     date.append(x)
# date = " / ".join(date)
# print("The examination will start from : ", date)
#
# print("""
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615""")
#
# n = input("number: ")
# nn = n*2
# nnn = n*3
# n = int(n)
# nn = int(nn)
# nnn = int(nnn)
#
# print(n + nn + nnn)
#
# print("""
# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.""")
#
# print("""
# === Answer ===""")
#
# print(abs.__doc__)
#
# print("""
# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module. """)
#
# print("""
# === Answer ===""")
#
# year = int(input("Please enter a year: "))
# print(calendar.calendar(year))