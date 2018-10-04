with open("words.txt") as file1:
    with open("sentences.txt", "w") as file2:
        file2 = ""
        for line in file1:
            if line.strip() == ".":
                file2 += line.strip()
                file2 += " \n"
            elif line.strip() != "":
                file2 += line.replace("\n", "")
                file2 += " "
        print(file2)



