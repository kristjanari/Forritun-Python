a = int(input("Please input an integer: "))

if a < 0 :
    print("Too low")
elif a > 0 and a < 10 :
    print("Less than 10")
elif a >= 10 and a < 20 :
    print("Between 10 and 20")
else :
  print("The value is too high!")