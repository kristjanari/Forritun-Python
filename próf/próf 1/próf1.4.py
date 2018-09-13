strengur = ""

for i in range(1,11):
    strengur += '\n'
    for j in range(1,11):
        strengur += ("{:>5}").format(str(i*j))

print(strengur)