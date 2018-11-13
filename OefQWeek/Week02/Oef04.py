# oefening 04

leeftijd = int(input("Gee de leeftijd van je hond in: "))

if(leeftijd < 0):
    {
        print("Dit is onmogelijk")
    }
elif(leeftijd == 1):
    {

        print("Uw hond is 14 jaar in hondenjaar.")
    }
elif(leeftijd == 2):
    {
        print("Uw hond is 22 in hondenjaar.")
    }
elif(leeftijd > 2):
    {
        print("Uw hond is {0} jaar oud in hondenjaren.".format(22+(leeftijd -2)*5))
    }