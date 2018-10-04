#sort_list() function goes here
def sort_list(listi):
    listi.sort()

def main():
    #loop to accept integers until a non-digit is entered goes here
    a_list = []
    while True:
        try:
            a_list.append(int(input()))
        except:
            break

    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()