#oefening 06
import random

vollelijst = ["EEN","TWEE","DRIE","VIER"]
volle_intlijst = [1,2,4,5,6,7,8,9,10]

def kies_element(lijst):
    getal = random.randint(0,len(lijst)-1)
    element = lijst[getal]
    return(element)



print("het gekozen nummer is " + kies_element(vollelijst))
el= kies_element(volle_intlijst)
print("het gekozen nummer is " + str(el))

