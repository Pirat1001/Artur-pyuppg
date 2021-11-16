# Artur Kaminski, TE20D
# moment02a och fördjupningen
# Det var ganska svårt att komma på hur man skulle kunna lösa uppgiften, men då jag använde mig av funktioner blev det mycket lättare

# Jag importerar en matematisk operatör för att kunna använda mig av "math.pi" som jag inte gjorde i grunduppgiften
import math

# Här definierar jag mina funktioner vilka inte fanns när jag klarade grunduppgiften
# Omkrets funktionen:
def multipio(a):
    return a * math.pi * 2.0
# Area funktionen:
def multipia(a):
    return a*a * math.pi

# Då jag klarade grunduppgiften använde jag mig av variabler som t.ex. omkrets och area som var tomma floats
# I fördjupningen behövde jag inte dessa

# Frågar användaren och dess radie i cm 
radie = float(input("Skriv in ditt radie i cm:"))

# I grunduppgiften använde jag mig av if satser för att räkna ut omkretsen och arean
# Nu i fördjupningen finns if satserna inte längre, här använder jag mig av funktioner som använder den inmatade radie värden
multipio(radie)
multipia(radie)
    

# Utskriften som berättar de tre olika värden som finns och jag använder mig av en placeholder för floating point number alltså 
# värden endast skrivs ut med två decimaler 
# Eftersom i grunduppgiften använde jag mig av tomma variabler omkrets och area ersattes dem till värden efter if satser
# här använder jag resultaten från funktionen för omkrets och resultaten av funktionen för arean
print("Cirkelns radie: {}cm ditt omkrets: {}cm och ditt area: {}cm\u00b2".format("%.2f" % radie,"%.2f" % multipio(radie), "%.2f" % multipia(radie)))