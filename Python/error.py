# Invalid input data_type error handling


while True:
    N = input("Enter the Number of Random Integers(N): ")
    try: 
        N = float(N)
        if N.is_integer():
            break
        else:
            print("Enter a integer value for N...")
    except ValueError:
        print("Enter a integer value for N...")

while True:
    lower_limit = input("Enter the Lower limit of the Distribution: ")
    upper_limit = input("Enter the Upper limit of the Distribution: ")
    try:
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)

        if isinstance(lower_limit, float) and isinstance(upper_limit, float):
            break
    except ValueError:
        print("Enter a integer/float value for lower and upper limit...")  