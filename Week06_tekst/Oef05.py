#oefening 05

studenten = {}

def inlezen_scores(bestand):
    f = open(bestand,"r")
    line = f.readline()
    while line:
        naam = line.split(":", [0]) #eerste element van de lijst nl 0
        temp = line.split(":") [1:]
        punten = []
        for score in temp:
            punten.append(int(score))

        line = f.readline()
    f.close()

def zoek_student(persoon):
    for naam in studenten:
