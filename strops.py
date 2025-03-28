# 1. GET SPAN OF STRING

def getSpan(input_string, substring): 
    if not input_string or not substring:
        return
    span_list = []
    string = len(input_string)
    sub_string = len(substring)
 
    for i in range(string - sub_string + 1):  
        if input_string[i:i+sub_string] == substring:  
            span_list.append((i, i + sub_string))  
 
    return (len(span_list), span_list)


# 2. REVERSE A STRING

def reverse_words(input_sentence):
    list_of_strings = list(input_sentence)
    print(list_of_strings)
    reversed_list = list_of_strings[::-1]
    reversed_sentence = "".join(reversed_list)
    print("Reversed sentence: ", reversed_sentence)
    
# 3. REMOVE PUNCTUATIONS

def removePunctuations(string):
    new_string = ''
    chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~''"
    for item in string:
        if item not in chars:
            new_string += item          
    print("Punctuation removed sentence: ") 
    print(new_string)
    
# 4. COUNT WORDS

def countWords(input_sentence):
    words = input_sentence.split()
    list_of_words = list(words)
    print(list_of_words)
    wordcount = len(list_of_words)
    print(f"Word count = {wordcount}")
    
# 5. CHARACTER MAP

def characterMap(input_string):
    output = {}
    for item in input_string.lower():
        if item in output.keys():
            output[item] = output[item]+1
        else:
            output[item] = 1
    print(output)

# 6. MAKE TITLE

def makeTitle(string):
    if(string.istitle()):
        print("The given string is already a Title")
    word_list = string.split()
    new_word = [word.capitalize() for word in word_list]
    capitalised_string = ' '.join(new_word)
    print("Title changed: ")
    print(capitalised_string)

# 7. NORMALISE SPACES

def normalizeSpaces(input_sentence):
    new_list = []
    space = False
    for item in input_sentence:
        if(item != ' '):
            new_list.append(item)
            space = False
        elif not space:
            new_list.append(' ')
            space = True
    converted_sentence = ''.join(new_list)     
    print("Converted sentence:", converted_sentence)

# 8. TRANSFORM

def transform(string):
    list_of_strings = list(string)
    print(list_of_strings)
    reversed_list = list_of_strings[::-1]
    reversed_sentence = "".join(reversed_list)
    new_sentence = reversed_sentence.swapcase()
    print("Translated/transformed sentence is:- ")
    print(new_sentence)
    
# 9. GET PERMUTATIONS

def get_permutations(string, count=0):
    if count == len(string):
        print("".join(string))  
        return
 
    for item in range(count, len(string)):
        string_list = list(string)
        string_list[count], string_list[item] = string_list[item], string_list[count]  
        get_permutations(string_list, count + 1) 
        
        
if __name__ == '__main__':
    
    # Testing get span
    
    getSpan("Playing and running", "ing")
    
    # Testing reverse a string
    reverse_words("microproject")
    
    # Testing remove punctuations
    removePunctuations("punct$uat$&*^^ions***")
    
    # Testing count words
    countWords("Malayalam")
    
    # Testing character map
    characterMap("Malayalam")
    
    # Testing make title
    makeTitle("this is for title")
    
    # Testing normalise spaces
    normalizeSpaces("This is    a test  for  normalize   space function")
    
    # Testing transform 
    transform("heLLoooOO")
    
    # Testing get permutations
    get_permutations("hat")