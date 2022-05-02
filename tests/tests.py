# from translator import english_to_french, english_to_german
import sys
from project.machinetranslation.translator import english_to_french, english_to_german

# A list of test words
text = [None, "World", "Good Morning, my name is Isaac"]

"""Using null input as "None" in list of test words throws error. 
So I decided to use try and exception. 
I printed the output the null input as a string "This is a null input" in French and German"""
print("\nOutput for english_to_french:")
for word in text:
    try:
        if word is None:
            # prints "This is a null input" in French
            print(english_to_french("This is a null input"))
        elif word is not None:
            print(english_to_french(word))
    except:
        print("Unknown Input")


print("\n\nOutput for english_to_German:")

for word in text:
    try:
        if word is None:
            # prints "This is a null input" in German
            print(english_to_german("This is a null input"))
        elif word is not None:
            print(english_to_german(word))
    except:
        print("Unknown Input")
