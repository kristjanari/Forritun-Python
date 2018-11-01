# SELECTED

# Eftirfarandi tafla sýnir þrjár dagsetningar og nafn viðkomandi frídaga:
# January 1 => New year's day
# June 17 => National holiday
# December 25 => Christmas day

# Skrifið forrit sem les inn nafn mánaðar og númer dags.
# Gera má ráð fyrir því að nafn mánaðar sé slegið inn í lágstöfum.
# Úr þessu inntaki skal búa til streng sem innheldur nafn mánaðarins,
# með fyrsta staf sem hástaf, ásamt númeri dagsins, með einu bili á milli. 
# Ef umræddur strengur er frídagur þá skal prenta út nafn viðkomandi frídags miðað við töfluna að ofan.
# Ef umræddur strengur er ekki frídagur þá skal prenta út "Not a holiday"
# Hint: Notið capitalize() fallið

# The following table shows three dates og names of the corresponding holidays:
# January 1 => New year's day
# June 17 => National holiday
# December 25 => Christmas day

# Write a program that prompts for the name of a month and a day number.
# You can assume that the month name is entered using lowercase letters.
# Using this input, you need to construct a string which contains the name of the month,
# with the first letter as uppercase, followed by the day number, with one space in between. 
# If the resulting string is a holiday then the program print the associated name according to the table above. 
# If the resulting string is a not holiday then the program prints "Not a holiday".
# Hint: Use the capitalize() function.

month = input("Month: ")
day = input("Day: ")

date_str = month.capitalize() + " " + day

if date_str == "January 1":
    print("New year's day")
elif date_str == "June 17":
    print("National holiday")
elif date_str == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")
