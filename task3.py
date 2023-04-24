#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]


import math
import typing

def Login():
    for i in range(0,3):
        U = str(input("Enter username:\n"))
        P = str(input("Enter password:\n"))
        if (U in users) and (P==passwords[users.index(U)]):
            print("Access Granted")
            return Login
        else:
            if i==2:
                print("Access Denied, too many failed attempts")
            elif i==0:
                print("Access Denied, two attempts remaining")
            else:
                print("Access Denied, one attempt remaining")



Login()