#The actual recursive function is here:
def multiply_by_adding(x:int,y:int):
    x= abs(x)
    y=abs(y)
    if y==1:
        return x
    else:
        return x + multiply_by_adding(x,y-1)

print(">>>>>>Multiply by Adding<<<<<<<")
#Taking in input
x_value: int = int(input("Enter the first number: "))
y_value:int = int(input("Enter the second number: "))

#Deciding what to output
#If any value is 0 the product is 0
if x_value==0 or y_value==0:
    print(0)

# #If both values are negative the product is the same as positive
# elif x_value<0 and y_value<0:
#     result=multiply_by_adding(x_value,y_value)
#     print(result)

#If one of the two values are negative the product is negative
elif x_value<0 or y_value<0:
    result=multiply_by_adding(x_value,y_value)*-1
    print(result)

#Otherwise just do the thing
else:
    print("Your product is: ")
    print(multiply_by_adding(x_value,y_value))