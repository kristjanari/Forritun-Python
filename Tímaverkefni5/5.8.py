stars = int(input("Max number of stars: ")) # Do not change this line
for i in range(1,2*stars):
    strengur = ""
    if i <= stars:
        for j in range(0,i):
            strengur += "*"
        print(strengur)
    if i > stars:
        strengur = ""
        for k in range(2*stars-i,0,-1):
            strengur += "*"
        print(strengur)
      