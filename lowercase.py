casual_input = input("Enter a word to make it in lowercase: ")

# function to convert casual words in lowercase

def lowercase_func(casual_input):
    lowercase = casual_input.lower()
    return casual_input, " - to lowercase is : " , lowercase

conv_lower = lowercase_func(casual_input)

# print the function on the terminal

print(conv_lower)
