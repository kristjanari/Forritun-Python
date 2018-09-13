mánuður = input("Month: ")
mánaðardagur = input("Day: ")

strengur = mánuður.capitalize() + " " + mánaðardagur

if strengur == "January 1":
    print("New year's day")
elif strengur == "June 17":
    print("National holiday")
elif strengur == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")