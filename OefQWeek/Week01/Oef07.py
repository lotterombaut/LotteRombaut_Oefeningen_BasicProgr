#week 1 oefening 07

minuten = int(input("Geef het aantal minuten in: "))
uren = int(input("Geef een aantal uren in: "))
dagen = int(input("geef het aantal dagen in: "))

seconden = (dagen *86400) + (uren *3600) + (minuten *60)

print("Het totale aantal seconden bedraagd {0}".format(seconden))