#Jag ändrade variabeln penna till att värden är int istället för ett bestämmd antal
penna = int
apple = float

#Nu finns också frågan med om hur många äpplen man vill köpa
fr = int(input("Hur många äpplen vill du köpa?(heltal)"))

fr1 = float(input("Hur mycket väger äpplen i kg?"))

#Samt hur många pennor man vill köpa
fr2 = int(input("Hur många pennor vill du köpa?(heltal)"))

pennor = fr2 * 3

pris = fr1 * 19.0

totalt = pris + pennor 

#Jag la till en utskrift i form av kvitto
print("""
Penna, {}st á 3kr        {} kr
Äpplen, {}g á 19kr/kg  {} kr
------------------------------
Summa                   {} kr
""".format(fr2, pennor, fr1, pris, totalt))

#Dessutom behövde jag ändra utskrifterna så att antalet finns med alltså t.ex. antalet pennor
print("Jag handlade {} pennor för {}kr och {} äpple för {}kr vilket totalt blev {}kr".format(fr2, pennor, fr, pris, totalt))

print(f"Jag handlade {fr2} pennor för {pennor}kr och {fr} äpple för {pris}kr vilket totalt blev {totalt}kr")

print("Jag handlade " + str(fr2) + " pennor för "  + str(pennor) + " kr och " + str(fr) + " äpple för "  + str(pris) + " kr vilket totalt blev "  + str(totalt) + "kr")

print("Jag handlade", fr2," pennor för", pennor,"kr och", fr, " äpple för", pris,"kr vilket totalt blev", totalt,"kr")