# Första lösningen 
# Importerar klockan och localtime funktionen
import time

# skapar en variabel för funktionen localtime()och berättar att jag vill ta ut timmar ifrån tuplen
timme = (time.localtime().tm_hour)

# skapar en if sats där jag skapar villkor att ifall klockan är större än 16 kommer det att skriva slut för dagen, om det är inte större än 16 är det
# en else sats som berättar att några timmar kvar, ifall klockan inte är större än 8 skriver det ut att du har inte börjat ännu. 
if timme > 16:
    print("kl. 8 - 16, skoldagen pågår") 
elif timme < 8:
    print("kl. 0 - 7, skoldagen har inte börjat")
else: 
    print("kl. 17 - 23, skoldagen är slut")

# Andra lösningen
# Importerar klockan och localtime funktionen
import time

# skapar en variabel för funktionen localtime()och berättar att jag vill ta ut timmar ifrån tuplen
timme = (time.localtime().tm_hour)

# skapar en if sats där jag skapar villkor att ifall klockan är större än 16 kommer det att skriva slut för dagen, om det är inte större än 16 är det
# en else sats som berättar att några timmar kvar, ifall klockan inte är större än 8 skriver det ut att du har inte börjat ännu. 
if timme > 8 and timme < 16:
    print("kl. 7 - 16, skoldagen pågår")
elif timme < 8:
    print("Du har inte börjat än")
else: 
    print("Slut för dagen")

# Tredje lösningen
# Importerar klockan och localtime funktionen
import time

# skapar en variabel för funktionen localtime()och berättar att jag vill ta ut timmar ifrån tuplen
timme = (time.localtime().tm_hour)

# skapar en if sats där jag skapar villkor att ifall klockan är större än 16 kommer det att skriva slut för dagen, om det är inte större än 16 är det
# en else sats som berättar att några timmar kvar, ifall klockan inte är större än 8 skriver det ut att du har inte börjat ännu. 
if timme > 16 or timme < 8: 
    print("Du har inte börjat än")
elif timme < 16 and timme > 8:
    print("Skoldagen pågår")