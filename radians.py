import random
import math

# Script I wrote to test a small process that converts radians to degrees without having to use a calculator.
# This process only works with the given denominators as they are factors of 180.

# j = numerator
# k = denominator

# 1. t = k / 6
# 2. p = 30/t        
# 3. degrees = j * p 
# -------------------------------------------------------------------------------------
# Ex. 11π / 12
# t = 12/ 6 or t ==2
# p = 30/2  or p == 15
# 11*15 = 155, so 11π / 12 == 165°

def convertRadians(numerator,denominator):
	denomList = [6,12,18,36,60,90]

	if denominator not in denomList:
		result = "you done messed up"
	else:
		numDivideThirtyBy = denominator/6
		thirtyDiv = 30/numDivideThirtyBy
		degrees = thirtyDiv * numerator
		result = round(degrees,2)
	return result


# This is the actual formula to convert from radians to degrees: degrees = radians * 180/π
def convertRadiansProper(numerator,denominator):
	theRadians = (math.pi * numerator) / denominator
	formula = (180/math.pi)
	final = theRadians * formula
	final = round(final,2)
	conversion = str(numerator)+"π /"+ str(denominator) + " = " + str(final) + "° "
	return conversion

# Test to compare process with regular formula
# Chooses random denominator from given list
def test1():
	for num in range(1,20):
		denomList = [6,12,18,36,60,90]
		randomDenom = random.choice(denomList)
		final = convertRadians(num,randomDenom)
		string1 = str(num)+"π /" + str(randomDenom) + " = " + str(final) + "°"

		# Using actual formula
		properConversion = convertRadiansProper(num,randomDenom)
		# if final == properConversion:
		#	comparison = True
		result = string1 + "\n" + str(properConversion) + "\n"
		print(result)


test1()