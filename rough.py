'''
ARITHMETIC CALCULATOR USING ENCAPSULATION AND NESTED IF CONCEPT

'''


class arithmetic_operators():
    print(".....ARITHMETIC CALCULATOR.....")
    number1 = int(input("Enter First the number.....:"))
    number2 = int(input("Enter the Second number.....:"))
    ADDITION = number1+number2
    SUBTRACTION = number1-number2
    MULTIPLICATION = number1*number2
    DIVISION = number1/number2
    MODULO = number1%number2
    MULTIDIVISION = number1//number2
    SQUARE = number1**number2


    def addnumbers(self):


        print("Addition is",self.ADDITION)
    def subtractionnumbers(self):

        print("Subtraction is",self.SUBTRACTION)
    def multiplication(self):

        print("Multiplication is",self.MULTIPLICATION)
    def Division(self):

        print("Division is",self.DIVISION)
    def Modulo(self):

        print("Modulo is",self.MODULO)

    def Multidivision(self):

        print("Multidivision is",self.MULTIDIVISION)
    def exponent(self):
        print("Square is",self.SQUARE)
a1 = arithmetic_operators()

def calculator():
    print("ADDITION-1\nSUBTRACTION-2\nMULTIPLICATION-3\nDIVISION-4\nMODULO-5\nMULTIDIVISION-6\nSQUARE-7\n")
    option = int(input("ENTER THE OPTION.....:"))
    if option == 1:
        a1 = arithmetic_operators()
        a1.addnumbers()
    elif option == 2:
        a1 = arithmetic_operators()
        a1.subtractionnumbers()
    else:
        if option == 3:
            a1 = arithmetic_operators()
            a1.multiplication()
        elif option == 4:
            a1 = arithmetic_operators()
            a1.Division()
        elif option == 5:
            a1 = arithmetic_operators()
            a1.Modulo()
        elif option == 6:
            a1 = arithmetic_operators()
            a1.Multidivision()
        elif option == 7:
            a1 = arithmetic_operators()
            a1.exponent()
        else:
            print("type only 1,2,3,4,5,6")


calculator()




