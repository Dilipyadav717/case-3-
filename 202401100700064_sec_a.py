# -*- coding: utf-8 -*-
"""202401100700064_sec_A.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UlgHzqvOOp6B9J2NSSxat4oOHcHq5g1V
"""

#case 3 : Develop a function to monitor temperature & provide alert
import random
def reading():
    temp = random.uniform(0,200)
    return temp
    print(f"Current temperature:{temperature}")


lower=int(input("Enter lower temperature: "))
upper=int(input("Enter upper temperature: "))
if (temp<lower):
    print("Temperature is too low")
elif(temp>upper):
    print("Temperature is too high")
else:
  print("temprature normal")
temp=reading()
print(f"temperature:{temp}")

