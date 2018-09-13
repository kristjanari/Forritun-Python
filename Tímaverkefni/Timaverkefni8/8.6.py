# Your function definition goes here
def fibo(n):
    tala1 = 0
    tala2 = 1
    ný_tala = 0
    strengur = "1 "
    for i in range(1,n):
        ný_tala = tala1 + tala2
        strengur += str(ný_tala) + " "
        tala1 = tala2
        tala2 = ný_tala
    return strengur

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here
print(fibo(n))        