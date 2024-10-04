# creating a function
def get_matrix(n , m ,value):

    matrix = [] # create an empty list

    for i in range(n): # create a external cycle

        matrix.append([]) # adding it to an empty list

        for j in range(m): # inner cycle

            matrix[i].append(value) # adding inner third value

    return matrix # ending function


# adding function in variable
result_1 = get_matrix(9, 17, 77)
result_2 = get_matrix(5,1,999 )
result_3 = get_matrix(22,13, 4)

# output of the console
print(f'the function with the first values:{result_1}\n with other values: {result_2}\n and with {result_3}')


