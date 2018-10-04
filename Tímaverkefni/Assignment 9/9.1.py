strengur = ""
strengur2 = ""
with open("test.txt", "r") as f:
    for line in f:
        strengur += line

strengur = strengur.replace("\n ", "")
print(strengur.replace(" ", ""))