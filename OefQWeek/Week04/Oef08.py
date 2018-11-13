#Oefening 08
lijst = [5,7,3,0,23,32,56,1358,9,17,92,76]

def som_get_lijst(parameter):
    som = 0
    for getal in parameter:
        som = som + getal
    return som

print(str(som_get_lijst(lijst)))