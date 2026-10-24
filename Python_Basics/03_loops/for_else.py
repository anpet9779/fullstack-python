# Else : works as final statement where after loop we can give default statement which has to run in all cases 

staff = [("Amit", 16), ("Zara", 15), ("Raj", 14) ]

for name, age in staff :
    if age >= 18:
        print(f"{name} is eligible")
        break
else:
    print(f"No one is eligible")

""" 
ELSE == aslo called as fallback 

In practical use  : If we are looking for any user in list based on some criteria but couldn't find anyone then else can print "No user found" 

"""

