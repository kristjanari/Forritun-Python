# SELECTED

# Skrifið Python forrit sem les inn eina jákvæða heiltölu, n, frá notanda og skrifar síðan út 
# aðra hverja heiltölu frá n niður í 1, eina í hverri línu. 
# Úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.

# Write a Python program which reads a single positive integer, n, from the user and then writes out 
# every other integer from n down to 1, each integer in a separate line.
# The output of the program should be exactly the same as shown in the example below.

# Example input/output:
# Input an integer: 10
# 10
# 8
# 6
# 4
# 2

n = int(input("Input an integer: "))

for i in range(n, 0, -2):
    print(i)