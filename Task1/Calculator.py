#Calculator

def calculator():
    print('Calculate Basic DMAS Operations\n')
    #Enter Operands and Operators
    operator_1 = int(input("Enter First Number  "))
    operator_2 = int(input("Enter Second Number  "))
    operand = input('Enter the Operand for Calculation ')
    if operand == '+':
        print('Performing Addition Operation ')
        print(f'{operator_1}  {operand}  {operator_2}')
        print(operator_1+operator_2)
        
    elif operand == '-':
        print('Performing Subtraction Operation ')
        print(f'{operator_1}  {operand}  {operator_2}')
        print(operator_1-operator_2)
        
    elif operand == '*':
        print('Performing Multiplication Operation ')
        print(f'{operator_1}  {operand}  {operator_2}')
        print(operator_1*operator_2)
        
    elif operand == '/':
        print('Performing Division Operation ')
        print(f'{operator_1}  {operand}  {operator_2}')
        print(operator_1/operator_2)
        
    elif operand == '%':
        print('Performing Remainder Operation ')
        print(f'{operator_1}  {operand}  {operator_2}')
        print(operator_1%operator_2)
        
    else: 
        print('Wrong Operand Entered.Try Again \n')
        
        
#Function Call
if __name__ == '__main__':
	calculator()