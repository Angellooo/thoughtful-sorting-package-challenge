def sort(width:int|float, height:int|float, length:int|float, mass:int|float):
    '''
    This function returns a string. It represent the name of the stack where the package should go. Either "STANDARD", "SPECIAL" or "REJECTED".
    \n*Args:\n
    width - int | float: The width of the package (Centimeters - cm).\n
    height - int | float: The height of the package (Centimeters - cm).\n
    length - int | float: The length of the package (Centimeters - cm).\n
    mass - int | float: The weight of the package (Kilograms - kg).
    '''
    # Booleans that indicate if a package is either Bulky or Heavy
    bulky = False
    heavy = False
    # Dimension and mass limits
    dim_limit = 150
    total_dim_limit = 1000000
    mass_limit = 20

    # Define if a package is Bulky depending on its dimensions
    if (width >= dim_limit or height >= dim_limit or length >= dim_limit) or ((width * height * length) >= total_dim_limit):
        bulky = True

    # Define if a package is Heavy depending on its weight/mass
    if mass >= mass_limit:
        heavy = True

    # Assign where the package should go
    if bulky == True and heavy == True:
        response_str = "REJECTED"
    elif bulky == True or heavy == True:
        response_str = "SPECIAL"
    else:
        response_str = "STANDARD"

    return response_str

    
if __name__ == "__main__":
    # Quick tests - For a more detailed use of test cases, go to test_sort_package.py
    print(sort(80, 80, 100, 10))  # Expected Output: STANDARD
    print(sort(20, 20, 20, 5))  # Expected Output: STANDARD
    print(sort(200, 100, 80, 10))  # Expected Output: SPECIAL
    print(sort(20, 10, 10, 250))  # Expected Output: SPECIAL
    print(sort(500, 400, 300, 50))  # Expected Output: REJECTED