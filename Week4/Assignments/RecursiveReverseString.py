def reverse_string(input_string:str):
    #Make the string a list
    char_list = list(input_string)

    #Manipulate
    #If the length is only one then there is only one character return it
    if len(char_list)==1:
        return char_list.pop(0)
    else:
        #Otherwise remove the last character from the list
        x = char_list.pop(-1)
        #Create a new string
        new_string:str =""
        #This loop only exists to make the characters list to go back to a string
        #I did not find a function to do it directly
        for char in char_list:
            new_string= new_string+char
        #This is the general case, return the last character of the string and call the funciton again
        return x + reverse_string(new_string)

if __name__=="__main__":
    print(">>>>>>>>>Recursive Reverse String<<<<<<<<")
    input_value:str = input("Enter the string to be reversed: ")
    print(reverse_string(input_value))
