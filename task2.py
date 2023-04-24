#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

import math
import typing

def Login():
    for i in range(0,3):
        U = str(input("Enter username:\n"))
        P = str(input("Enter password:\n"))
        if U==expectedUsername and P==expectedPassword:
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