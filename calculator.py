# This program forever runs a calculation between 2 numbers given by the user with an operator
# Extra points: I made it check for invalid input issues and 0 division, it makes sure the inputs are valid and can never print errors.

def getNum(): # Asks for a number and returns it if it's a valid number.
    num = input("Enter valid number: ")
    try:
        num = float(num)
        return num #Return the inputted number
    except:
        print("Your input is not a valid number! Try again.")
        return 'invalid' #Getting a valid number did not work.

def printAnswer(n1,n2,operator,answer): # simply print the full equation with the given numbers
    print(str(n1),operator,str(n2),"=",str(answer))

def calculate(): # Try to calculate something
    n1 = getNum()
    if n1 != 'invalid': # If n1 got a valid number input the user
        print("Now enter a second number.")
        n2 = getNum()
        if n2 != 'invalid': # If n2 and n1 are both valid numbers
            operator = input("Enter valid operation (+,-,*,/,^): ")
            # Now check for every operator and define/print out the answer of the equation
            if operator == '+' or operator.lower() == 'add': #addition
                answer = n1 + n2
                printAnswer(n1,n2,'+',answer)
            elif operator == '-' or operator.lower() == 'subtract': #subtraction
                answer = n1 - n2
                printAnswer(n1,n2,'-',answer)
            elif operator == '*' or operator.lower() == 'multiply': #multiplication
                answer = n1 * n2
                printAnswer(n1,n2,'x',answer)
            elif operator == '/' or operator.lower() == 'divide': #division
                if n2 != 0: #Check for 0 division
                    answer = n1 / n2
                    printAnswer(n1,n2,'/',answer)
                else:
                    print("Diving by 0 is not possible! Try again.")
            elif operator == '^' or operator == '**' or operator.lower() == 'exponent': #exponent
                answer = n1 ** n2
                printAnswer(n1,n2,'^',answer)
            else: # if the inputted operation wasn't a valid operation
                print("Your operation was not valid! Try again.")
                
while True: # Forever loop the calculate function
    calculate()