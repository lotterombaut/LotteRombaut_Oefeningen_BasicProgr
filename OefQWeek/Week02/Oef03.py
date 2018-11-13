# oefening 03
from datetime import datetime

geboortejaar = int(input("Geef uw geboortejaar in: "))
nu = datetime.now().year
datum = datetime.now().date()

if(nu- geboortejaar >= 18):
    {
        print("Je bent oud genoeg.")
    }
else:
    {
        print("Je bent niet oud genoeg")
    }

print(datum)
