#This function is meant to check if the number{num} is divisible by decreasing values of x
def check_if_prime_recursion(num,x):

    #If after all the decreasing we find that x is 1 -> it is prime
    if x == 1:
        print("The number entered is prime!")

    #Else if x is not 1
    else:
        #If number is divisible by x, get out of the function and say it is divisible by x
        if num % x == 0:
            print("The number entered is divisible by: "+ str(x))
            print("The number is not Prime!")
            return
        #Else if is not divisible by x, check the divisibility with the next lower value of x
        else:
            check_if_prime_recursion(num,x-1)

#This function allows us to just take in one function arguement
def check_if_prime(num:int):
    #It's implementation will just take the next lower value and begin the check from there
    check_if_prime_recursion(num,num-1)

if __name__=="__main__":
    print(">>>>>>>>Test For Prime<<<<<<<<<<")
    number:int = int(input("Enter the integer value to be checked: "))
    check_if_prime(number)


