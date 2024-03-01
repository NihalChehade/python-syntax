
def print_upper_words(strList):
    """print out each word on a separate line, uppercased """

    for str in strList:
        print(str.upper())

def print_upper_words2(strList):
    """prints words that start with the letter ‘e’ (either upper or lowercase) """

    for str in strList:
        if str.startswith("e") or str.startswith("E"):
            print(str.upper())

def print_upper_words3(strList, must_start_with):
    """pass in a set of letters, and only prints words that start with one of those letters"""
   
    for str in strList:
        for char in must_start_with:
            if str.startswith(char):
                print(str.upper()) 

        

    
    
    



    
