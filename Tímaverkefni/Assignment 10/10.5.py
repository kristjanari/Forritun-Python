def input_vector(stærð):
    listi = []
    for i in range(stærð):
        listi.append(float(input("Element no {}: ".format(i+1))))
    return listi    

def dot_product(vigur1, vigur2):
    tala = 0
    for i in range(size):
        tala += vigur1[i]*vigur2[i]
    return float(tala)


# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))