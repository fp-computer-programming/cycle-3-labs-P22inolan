# Author: IBN (AMDG) 9/30/2021
magic_charge = int(input("What is your magic strength? "))
shield_charge = int(input("What is your shield charge? "))

if (magic_charge) < 90 and (shield_charge) < 75:
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")
