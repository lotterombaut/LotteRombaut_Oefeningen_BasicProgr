#oefeming 02

tuple = ("1NMCT", "2NMCT", "3NMCT")

def print_tuple(parameter):
    element = 0
    index = 0
    for i in parameter:
        element = parameter[index]
        index = index + 1
        print(str(element) + "staat op postitie" + str(index))



print("verzameling:")
print(print_tuple(tuple))