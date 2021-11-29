#skapar variabler för de två olika input(frågor) och definierar vilket datatyp de har för programmen
age = int(input("Hur gammal är du?: "))
name = str(input("Vad heter du?: "))

# tar bort onödiga blankspaces
name = name.strip()

#skapar en if sats där utskriften skiljer sig beroende på ifall man är myndig eller ej
if age >= 18:
    print("Du heter {}, första bokstaven i ditt namn är {} och du är myndig".format(name, name[0]))
else: 
    print("Du heter {}, första bokstaven i ditt namn är {} och du är omyndig".format(name, name[0]))