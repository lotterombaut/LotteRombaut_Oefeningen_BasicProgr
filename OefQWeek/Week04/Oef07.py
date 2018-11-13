#oefening 07

lijst = [5,7,3,0,23,32,56,1358,9,17,92,76]

def max_num_in_list(num_list):
    grootste = 0
    for i in num_list:
        if(i > grootste ):
            grootste = i
    return grootste

print(str(max_num_in_list(lijst)))
