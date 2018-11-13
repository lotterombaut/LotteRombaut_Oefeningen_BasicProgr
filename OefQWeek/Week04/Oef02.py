#oefening 2

list_friends = []
i = 0

while i != "":
    i = input("Geef de naam van een vriend in, of sluit af met een leeg veld: ")
    list_friends.append(i)

list_friends.pop()
print(list_friends)