tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)


def multiple(input_tuple):
    result = 1  

    for i in input_tuple: 
        result = result * i

    
    print(f"The final result is {result} for all the multiples of the tuple!")
    return result


multiple(tup1)
multiple(tup2)
