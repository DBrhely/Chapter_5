#Challenge 2
#12/17/14
#Danielle Brhely

#Design
#create a program that spend pool point to four attributes
#make sure that the spend is use
#take some point away if the user want to decrease the attributes value
#print the attributes
###############################
pointpool = 30
STR = 0
HP = 0
DEX = 0
WIS = 0
addRem = ""
print("-----MENU------")
print("Point avalible", pointpool)
print("1 - Strength", STR)
print("2 - Health", HP)
print("3 - Wisdom", WIS)
print("4 - Dexterity" , DEX)
print("0 - Quit")
print()
code = int(input("Enter a number. "))
while code != 0:
    if code == "1":
        if addRem == "add":
            point = int(input("How many point do you want to add? "))
            check = pointpool - points
            if check < 0:
                print("Not enough point.")
            else:
                STR = STR + points
                pointpool = pointpool - points
        elif addRem == "rem":
            if check < 0:
                point = int(input("How many point do you want to add? "))
                print("Too many point.")
            else:
                STR = STR + points
                pointpool = pointpool - points
        else:
            print("Invaild input.")
    elif code == "2":
         if addRem == "add":
             points = int(input("How many point do you want to add? "))
             check = pointpool - points
             if check < 0:
                print("Not enough point.")
             else:
                 HP = HP + points
                 pointpool = pointpool - points
         elif addRem == "rem":
             if check < 0:
                 points = int(input("How many point do you want to add? "))
                 print("Too many point.")
             else:
                 HP = HP + points
                 pointpool = pointpool - points
         else:
             print("Invaild input.")
    elif code == "3":
        if addRem == "add":
             point = int(input("How many point do you want to add? "))
             check = pointpool - points
             if check < 0:
                 print("Not enough point.")
             else:
                 WIS = WIS + points
                 pointpool = pointpool - points
        elif addRem == "rem":
            if check < 0:
                 point = int(input("How many point do you want to add? "))
                 print("Too many point.")
            else:
                 WIS = WIS + points
                 pointpool = pointpool - points
        else:
            print("Invaild input.")
    elif code == "4":
        if addRem == "add":
            point = int(input("How many point do you want to add? "))
            check = poolPoint - points
            if check < 0:
                 print("Not enough point.")
            else:
                 DEX = DEX + points
                 pointpool = pointpool - points
        elif addRem == "rem":
            if check < 0:
                 point = int(input("How many point do you want to add? "))
                 print("Too many point.")
            else:
                 DEX = DEX + points
                 pointpool = pointpool - points
        else:
             print("Invaild input.")
    else:
         print("Invalid code.")
    print()
    print("-----MENU------")
    print("Point avalible", pointpool)
    print("1 - Strength", STR)
    print("2 - Health", HP)
    print("3 - Wisdom", WIS)
    print("4 - Dexterity" , DEX)
    print("0 - Quit")
    print()
    code = int(input("Enter a number. "))

#Final result
print("----------")
print("Final Points")
print("Point Remain", pointpool)
print("Strength", STR)
print("Health", HP)
print("Wisdom", WIS)
print("Dexterity", DEX)


input("\nPress <Enter> to exit......")










