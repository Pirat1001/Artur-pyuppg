

penna = 4
pennor = penna * 3
apple = float

fr = float(input("Hur mycket väger äpplet i kg?"))

pris = fr * 19.0

totalt = pris + pennor 

print("Jag handlade 3 pennor för {}kr och 1 äpple för {}kr vilket totalt blev {}kr".format(pennor, pris, totalt))

print(f"Jag handlade 3 pennor för {pennor}kr och 1 äpple för {pris}kr vilket totalt blev {totalt}kr")

print("Jag handlade 3 pennor för"  + str(pennor) + "kr och 1 äpple för"  + str(pris) + "kr vilket totalt blev"  + str(totalt) + "kr")

print("Jag handlade 3 pennor för", pennor,"kr och 1 äpple för", pris,"kr vilket totalt blev", totalt,"kr")