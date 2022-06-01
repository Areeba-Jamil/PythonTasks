#Decimal to Binary Converter
def converttobinary():
    Num = int(input('Enter Decimal Number:'))
    print('Converting Decimal to Binary')
    print('Binary Number:')
    return bin(Num).replace("0b","")


print('\n')
def binarytodecimal():
    B2D = input('Enter Binary Number:')
    print('Converting Binary to Decimal')
    print('Decimal Number:')
    converted_n = int(B2D, 2)
    print(converted_n)


# Methods Call
if __name__ == '__main__':
    print(converttobinary())
    print(binarytodecimal())