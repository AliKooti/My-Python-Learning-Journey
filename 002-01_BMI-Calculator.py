"""
PEMDAS rule:
() Parenthesis
** Exponentiation
*  Multiplication
/  Division
+  Addition
-  Subtraction
"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / (float(height)**2)
print(int(bmi))
