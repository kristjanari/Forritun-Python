# SELECT
# Skrifið Python forrit sem les inn tvær heiltölur frá notanda.
# Fyrri talan stendur fyrir upphafsgildi á röð og seinni talan stendur fyrir mismun á sérhverjum samliggjandi gildum raðarinnar.
# Forritið skrifar síðan út sérhvert gildi raðarinnar (með einu bili á milli gilda) þangað til summa gildanna er orðin >= 100.
# Í lokin skrifast jafnframt út summan.

# Write a Python program which reads two integers from the user. 
# The first integer denotes the initial value of a series and the second integer denotes the difference between any two consecutive values in the series.
# The program then writes out each value of the series (with one space between values) until the sum of the values is >= 100.
# Finally, the sum is written out.

# Example input/output:
# Initial value: 1
# Step: 4
# 1 5 9 13 17 21 25 29
# Sum of series: 120

value = int(input("Initial value: "))
step = int(input("Step: "))

max_sum = 100
sum = 0

while sum < max_sum:
        print(value, end=' ')
        sum += value
        value += step

print("")
print("Sum of series:", sum)