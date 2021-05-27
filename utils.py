import math
from datetime import datetime

def Area(Radius):
  Area = math.pi * pow(Radius, 2)
  return Area

def name(Fname,Lname):
    return "Hello  " + Lname + " " + Fname

def getdatetime():
    currentDateTime = datetime.now()
    return currentDateTime


