# Build a program that calculates the number of characters in a string
# eg. count_characters("its a fantastic day", "a") #=> 4

# Parameters
#    - text, a string (eg. "life is amazing")
#    - character, a string (eg. "e")
# Returns
#    - integer (eg. 4)
# Side effects
#    - None
def count_characters(text, character):
    txt = text
    x = txt.count(character)
    return x

print(count_characters("Its a fantastic day", "a"))
print(count_characters("Feeling very confident", "e"))
print(count_characters("Testing my coding", "g"))

# Tasks 
# - read through text string
# - for each instance of character count
# - count is (+ 1) (maybe for loop or variable)