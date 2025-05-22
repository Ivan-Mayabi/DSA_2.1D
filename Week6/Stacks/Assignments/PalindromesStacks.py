class Stacks:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True

    def pop(self):
        #Edge case 1: Nothing to pop
        if len(self.data) == 0:
            print("This is an empty list")
            return
        #Normal cases
        else:
            x = self.data.pop(-1)
            return x

    def push(self,data):
        #Normal cases
        self.data.append(data)

    def peek(self):
        return self.data[-1]

    def length(self):
        return len(self.data)

if __name__=="__main__":
    stck1 = Stacks()

    #Accept some input
    entered_string = input("Place the string to be tested:\n")


    if len(entered_string) <= 50 and len(entered_string)>=1:
        # For each character push it into a stack
        for character in entered_string:
            stck1.push(character)

        # Create a list
        output_list = []

        # For each item in the stack, pop from the top and place in a list
        while stck1.length() != 0:
            output_list.append(str(stck1.pop()))

        output_string = "".join(output_list)

        if output_string == entered_string:
            print(f"The word {entered_string} is a palindrome")
        else:
            print(f"The word {entered_string} is not a palindrome")
    else:
        print("The string is too long")