invoer_seconden = int(input("Geef een aantal seconden op: "))

minuten = invoer_seconden/60
uren = invoer_seconden/ 3600
dagen = invoer_seconden /86400

print("DD:UU:MM:SS ==> {0}:{1}:{2}".format(dagen, uren, minuten))