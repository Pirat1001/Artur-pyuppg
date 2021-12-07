# Importerar tidsfunktioner
import time 

# Skapar en funktion för tiden som använder två inmatade värden
def timme(a, b):
    # Om klockan är större eller lika med a och klockan är mindre än b pågår skoldagen
    if (time.localtime().tm_hour) >= a and (time.localtime().tm_hour) < b:
        return ("skoldagen pågår")
    # Annars om klockan är mindre än a har skoldagen inte börjat än
    elif (time.localtime().tm_hour) < a:
        return ("Skoldagen har inte börjat")
    # Annars är det slut för skoldagen
    else:
        return ("Slut för skoldagen")

#Frågar om tiden alltså när skoldagen för en börjar och slutar
q_1 = float(input("När börjar du: "))
q_2 = float(input("När slutar du: "))

# Stoppar in de inmatade värden som argumenter i funktionen 
klockan = timme(q_1, q_2)

# Skriver ut det värden som var sant i funktionen timme(a,b)
print(klockan)