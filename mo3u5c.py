import time 

def timme(a, b):
    if (time.localtime().tm_hour) >= a and (time.localtime().tm_hour) < b:
        return ("skoldagen pågår")
    elif (time.localtime().tm_hour) < a:
        return ("Skoldagen har inte börjat")
    else:
        return ("Slut för skoldagen")

q_1 = float(input("När börjar du: "))
q_2 = float(input("När slutar du: "))

klockan = timme(q_1, q_2)

print(klockan)