
# Skrifið Python forrit sem skrifar út margföldunartöfluna fyrir tölurnar 1-10 (báðar meðtaldar)

# Write a Python program that prints out the multiplication table for the numbers 1-10 (both inclusive).

# The result should look like this:
#    1    2    3    4    5    6    7    8    9   10
#    2    4    6    8   10   12   14   16   18   20
#    3    6    9   12   15   18   21   24   27   30
#    4    8   12   16   20   24   28   32   36   40
#    5   10   15   20   25   30   35   40   45   50
#    6   12   18   24   30   36   42   48   54   60
#    7   14   21   28   35   42   49   56   63   70
#    8   16   24   32   40   48   56   64   72   80
#    9   18   27   36   45   54   63   72   81   90
#   10   20   30   40   50   60   70   80   90  100

# The width for each number is 5, and each number is right justified.

MAX = 10
for i in range(1,MAX+1):
    for j in range(1,MAX+1):
        print("{:>5d}".format(i*j), end="")
    print("")