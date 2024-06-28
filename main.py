def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        try:
            Inpat= int(input('Enter Number'))
            number= float(Inpat)
        except ValueError:
            print('Input must be numeric!')
        else:
            print(f'Valid input:{number}')
            break
        
    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
