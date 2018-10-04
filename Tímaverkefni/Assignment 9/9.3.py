max_lengd = 0
lengsta_orð = ""
with open("words.txt") as f:
    for line in f:
        if len(line) > max_lengd:
            max_lengd = len(line.strip())
            lengsta_orð = line

lengsta_orð = lengsta_orð.strip()
print("Longest word is '{}' of length {}".format(lengsta_orð, max_lengd))