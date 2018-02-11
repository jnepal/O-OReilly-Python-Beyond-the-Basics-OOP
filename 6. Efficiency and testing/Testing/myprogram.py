

def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    return x * 2

'''
    This if Gate ensures that the statements inside this block
    is executed only if the file is compiled itself. i.e from the 
    main namespace and the code inside if block
    wont be executed if it is imported to other file
'''
if __name__ == "__main__":
    input_val = input()
    doubled_val = doubleit(input_val)

    print("The value of {0} is {1}".format(input_val, doubled_val))