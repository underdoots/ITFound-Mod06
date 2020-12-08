


# def fxn

# def ProcessSomething():
#     print ("I'm" )
#     print ("processing data")
#
# ProcessSomething()
#
# #def fxn
# def ProcessSomething(parmMessage):
#     print ("The parameter was: " + parmMessage)
# #call fxn
# ProcessSomething("arg ABC") # so here, "arg ABC" is the parameter

# def CalculateValues(value1, value2):
#     fltSum = value1 + value2
#     print ("The sum of the values is " + str(fltSum))
#     fltDiff = abs (value1 - value2)
#     print("The difference of the values is " + str(fltDiff))
#     fltQuo = value1/value2
#     print("The quotient of the values is " + str(fltQuo))
#     fltProd = value1*value2
#     print("The product of the values is " + str(fltProd))
# CalculateValues(10,5)

#LISTING 5
# #---data code---#
# fltV1 = None #1st arg
# fltV2 = None #2nd arg
#
# #processing code
# def AddValues (value1, value2):
#     fltAnswer = value1 + value2
#     print (fltAnswer);
# #presentation (I/O code)
# fltV1 = float(input("Enter Value 1: "))
# fltV2 = float(input("Enter Value 2 "))
# print ("The sum of %.2f and %.2f" % (fltV1, fltV2))
# #the %.2f apparently means that you're looking for a floating point value w/2 dec places. %.s would be string
# print ("is: ", end = "")
# AddValues(fltV1, fltV2)

#LISTING 6

#data code
# fltV1 = None #1st argument
# fltV2 = None
# fltR1 = None #1st result of processing; for things like sum, diff, quo, prod just swap instead of Rx
# fltR2 = None
# fltR3 = None
#
# #processing code
# def AddValues (value1 , value2):
#     fltAnswer = value1 + value2
#     return value1, value2, fltAnswer #PACK TUPLE****** - no () and using CSV automatically packs a tuple
#
# #presentation code (I/O)
# fltV1 = float(input("Enter value 1: "))
# fltV2 = float(input("Enter value 2: "))
# fltR1, fltR2, fltR3 = AddValues (fltV1, fltV2) #UNPACK TUPLE****
# print ("The sum of %.3f and %.2f is %.1f" % (fltR1, fltR2, fltR3))
#

#LISTING 11 - using none keyword,

#processing code
# def CalcValues (value1 = None, value2 = None, operation = None):
#     if value1 is None or value2 is None or operation is None: # is is an operator
#         fltAnswer = "Error: Missing Arguments" # error handling
#     elif operation.lower() == "+": fltAnswer = value1 + value2
#     elif operation.lower() == "-": fltAnswer = abs(value1 - value2)
#     elif operation.lower() == "/": fltAnswer = value1/value2
#     elif operation.lower() == "*": fltAnswer = value1*value2
#     else: fltAnswer = "Error"
#     return value1, operation, value2, fltAnswer #note this is a tuple
# #presentation
# print (CalcValues ())
# print (CalcValues(5,10))
# print (CalcValues(5,10, "*"))

#LISTING 13 Python's version of by value and by reference
# -- data code -- #
v1 = 5
v2 = 10
lstData = [0, 0, 0, 0]
dicData = {"sum": 0, "diff": 0, "prod": 0, "quot": 0}

# -- processing code -- #
def CalcListValues(value1, value2, all_answers):
    all_answers[0] = value1 + value2
    all_answers[1] = value1 - value2
    all_answers[2] = value1 * value2
    all_answers[3] = value1 / value2
def CalcDictionaryValues(value1, value2, all_answers):
    all_answers["sum"] = value1 + value2
    all_answers["diff"] = value1 - value2
    all_answers["prod"] = value1 * value2
    all_answers["quot"] = value1 / value2
# -- presentation (I/0) code -- #
CalcListValues(value1 = v1, value2 = v2, all_answers = lstData)
print(lstData)
CalcDictionaryValues(value1 = v1, value2 = v2, all_answers = dicData)
print(dicData)

#LISTING 17 - classes

class MathProcessor():
    """functions for processing simple math"""
    @staticmethod
    def AddValues(value1=0.0, value2=0.0):
        """this function adds two values
        :param1 value1: (float) first number to add
        :param2 value2: (float) 2nd number to add
        :return (float) sum of two numbers"""
        return float(value1 + value2)
    @staticmethod
    def SubValues(value1=0.0, value2 = 0.0):
        return float(value1 - value2)

#presentation I/O
print(MathProcessor.AddValues(5,19)) #need to refer to the class, use a . notation, then the fxn. called "drilling into the class"
print(MathProcessor.SubValues(5,19))

#see lab6-3.py for capturing user input and displaying it neatly
