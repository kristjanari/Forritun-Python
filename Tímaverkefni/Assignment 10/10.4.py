def make_new_row(row):
    if row == []:
        return [1]
    if row == [1]:
        return [1, 1]
    new_list = []
    for i in range(len(row)):
        if i == 0:
            new_list.append(1)
        else:
            pascal = row[i-1]+row[i]
            new_list.append(pascal)
    new_list.append(1)
    return new_list

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)