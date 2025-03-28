'''
This is a sample test app for the hackathon
Consists of :
    1. GET SPAN OF STRING
    2. REVERSE A STRING
    3. REMOVE PUNCTUATIONS
    4. COUNT WORDS
    5. CHARACTER MAP
    6. MAKE TITLE
    7. NORMALISE SPACES
    8. TRANSFORM
    9. GET PERMUTATIONS
    
'''


import strops

print("-"*80)
print("Enter 1 for GET SPAN OF STRING")
print("Enter 2 for REVERSE A STRING")
print("Enter 3 for REMOVE PUNCTUATIONS")
print("Enter 4 for COUNT WORDS")
print("Enter 5 for CHARACTER MAP")
print("Enter 6 for MAKE TITLE")
print("Enter 7 for NORMALISE SPACES")
print("Enter 8 for TRANSFORM")
print("Enter 9 for GET PERMUTATIONS")
print("-"*80)

choice = int(input())

if(choice == 1):
    input_string = input("Enter the string: ")
    substring = input("Enter the substring: ")
    count, span = strops.getSpan(input_string, substring)
    print(count, span)
elif(choice == 2):
    input_string = input("Enter the string: ")
    strops.reverse_words(input_string)
elif(choice == 3):
    input_string = input("Enter the string: ")
    strops.removePunctuations(input_string)
elif(choice == 4):
    input_string =  input("Enter the string: ")
    strops.countWords(input_string)
elif(choice == 5):
    input_string =  input("Enter the string: ")
    strops.characterMap(input_string)
elif(choice == 6):
    input_string =  input("Enter the string: ")
    strops.makeTitle(input_string)
elif(choice == 7):
    input_string =  input("Enter the string: ")
    strops.normalizeSpaces(input_string)
elif(choice == 8):
    input_string =  input("Enter the string: ")
    strops.transform(input_string)
elif(choice == 9):
    input_string =  input("Enter the string: ")
    strops.get_permutations(input_string)
else:
    print("Invalid choice")