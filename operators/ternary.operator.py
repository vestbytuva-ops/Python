#The Ternary Operator

#The ternary operator allows you to assign one value if a condition is true, and another if it is false:

num = 6

x = "WEEKEND" if num > 5 else "Workday"

print(x)

#Note: The Ternary operator is not an actual operator, it is a conditonal expression, or a shorthand if statement. 

#Instead of Elif:

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

#The output is Sat because the num variable is 6.
