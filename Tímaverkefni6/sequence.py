#Röðin byrjar á tölunum 1 og 2, síðan ræðst næsta tala af summu þeirra þriggja talana sem á undan komu(G.r.f að 0 sé á undan 1 við útreikning á staki 3)
#Biðjum notanda um að slá inn heiltölu n
#Búum til 4 breytur, teljara til að stjórna lengd raðar og 3 tölur sem við notum til að reikna næstu tölu í röðinni
#Byrjum á að prenta fyrstu tvær tölurnar, ef n >= 2
#Notum while lykkju til að fá út næsta stak í hvert skipti
#Notum breytuna bæt_við til þess að halda utan um summu fyrstu tveggja talnanna af þremur
#Hliðrum svo þeim tölum upp um 1 sæti til að undirbúa reikning í næstu umferð
#Leggjum summuna við þriðju töluna og prentum þá summu
#Höldum áfram þar til við erum komin með n stök í röðina og prentum hana




n = int(input("Enter the length of the sequence: ")) # Do not change this line

teljari = 0
tala1 = 0
tala2 = 1
tala3 = 2
bætum_við = 0
print(tala2)
if n > 1:
    print(tala3)

while teljari < n-2 and n > 1:
    
    bætum_við = tala1 + tala2
    tala1 = tala2
    tala2 = tala3
    tala3 += bætum_við
    print(tala3)
    teljari += 1



