#oefening 09

import random

oplossing = random.randint(1,20)
print(oplossing)
invoer = int(input("Raad het getal (1 tem 20): "))

while invoer != oplossing:
   invoer= int(input("Raad het getal (1 tem 20): "))


print("je hebt het juiste getal geraden! Proficiat!")
