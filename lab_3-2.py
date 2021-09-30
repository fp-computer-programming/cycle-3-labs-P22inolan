# Author: IBN (AMDG) 9/30/2021
points = input("How many points did the team score? ")
if int(points) <= 8:
    print("The team did not win a medal.")
elif int(points) <= 11:
    print("The team won a bronze medal.")
elif int(points) <= 14:
    print("The team won a silver medal.")
else:
    print("The team won a gold medal.")
