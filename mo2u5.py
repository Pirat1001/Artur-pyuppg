# Skriv en kommentar för varje fel du identifierar och löser.
# Beskriv vad som var fel och hur du har löst det.

#Här glömmer man en understräck vilket gör att variabeln blir ofylld alltså man vill att variabeln ska heta exchange_rate_dollar_to_sek 
#Jag lägger till ett understräck mellan rate och dollar
exchange_rate_dollar_to_sek = 8,82

#Man har inte tagit med "" på stringens ändar därför blir det fel
#Då jag lägger till dem skrivs ut meningen
print("Detta är ett program där vi kan växla mellan SEK & dollar")

#Här börjar man variabel namnet med ett tal vilket man inte kan göra. Samt stänger man inte stringen därför blir det fel, man glömmer ett ". 
#Jag tar bort ettan från 1sek och lägger till ett dubbelfnuff i slutet av stringen
sek = input("Hur många SEK vill du växla till dollar: ")

#Här har man fortfarande med den 1 i början av 1sek vilket man inte kan ha
dollar = sek / exchange_rate_dollar_to_sek

#1sek finns fortfarande med här i slutet efter .format samt har man glömt ett stängande parantes i slutet 
#Jag tar bort 1 från 1sek och lägger till stängande parantesen 
print("Du ville växla {0} SEK vilket blir {1} dollar.".format(sek, dollar))