#oefening 9

lijst = [5,7,3,0,23,32,56,1358,9,17,92,76]

def gemiddelde_in_lijst(parameter):
    gemiddelde = 0
    som = 0
    for i in parameter:
        som = som + i

    gemiddelde = som/len(parameter)
    return gemiddelde

print(str(gemiddelde_in_lijst(lijst)))