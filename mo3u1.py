# Importerar klockan och localtime funktionen
import time

# skapar en variabel för funktionen localtime()och berättar att jag vill ta ut timmar ifrån tuplen
timme = (time.localtime().tm_hour)

# skapar en if sats där jag berättar att ifall timmen är större än 16 ska det skriva ut "slut för dagen" 
if timme > 16:
    print("Slut för skoldagen!")
# Om timmen är inte större än 16 skriver den ut "Några timmar kvar"
else:
    print("Några timmar kvar!")