#Búum til breytu max_int = 0
#Búum til breytu n = 1, til ap komast inn í while lykkjuna
#Biðjum notanda um að slá inn jákvæða heiltölu heiltölu
#Ef hann slær inn jákvæða tölu athugum við hvort hún sé stærri en fyrri tölur, ef svo er þá verður hún max_int
#ef hann slær inn neikvæða tölu hættum við og prentum max_int

max_int = 0
n = 1
while n > 0:
    n = int(input("Input a number:"))
    if n > max_int:
        max_int = n
print(max_int)