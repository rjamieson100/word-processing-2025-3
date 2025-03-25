import getkey

#keep version number within 2 sig-digs (eg. v3.22)
version = "1.34"

words_list = []

#opens a text file called "words"
words_file = open("words.txt", "r")
while True:
    line = words_file.readline().strip()
    if line == "":
        break
    else:
        words_list.append(line)
words_file.close()

title = [" __    _            _ __                                ",
         "( /   /         /  ( /  )                    o          ",
         " / / /__ _   __/    /--'_   __ _, _  (   (  ,  _ _   _, ",
         "(_/_/(_)/ (_(_/_   /   / (_(_)(__(/_/_)_/_)_(_/ / /_(_)_",
         "                                                     /| ",
         "                    Version: " + version + "                   (/  "]

f_button = ["╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐",
            "╠╣ │ │││││   │ ││ ││││└─┐",
            "╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘"]

w_button = ["╦ ╦┌─┐┬─┐┌┬┐┌─┐",
            "║║║│ │├┬┘ ││└─┐",
            "╚╩╝└─┘┴└──┴┘└─┘"]

c_button = ["╔═╗┬─┐┌─┐┌┬┐┬┌┬┐┌─┐",
            "║  ├┬┘├┤  │││ │ └─┐",
            "╚═╝┴└─└─┘─┴┘┴ ┴ └─┘"]

functions = ["All Vowels", "Most Letters", "'Merica", "Backwards", "Odd/Even",
             "Wordle Panic","Crossword Solver", "Minus One", "Plus One", "Anagram",
             "Anagrams Minus One", "Here or There"]

authors = ["Farhan Mohammad", "Jun Li & Keith Marley", "Everett Campbell & Jasper Duff", 
           "Everett Campbell & Jasper Duff", "Everett Campbell & Jasper Duff", 
           "Olivia Chezzi", "Luca Bugliari-Goggia & Qui Loi Tran", 
           "Luca Bugliari-Goggia & Qui Loi Tran", "Luca Bugliari-Goggia & Qui Loi Tran",
           "Jun Li & Keith Marley", "Jun Li & Keith Marley", "Aidan McFadden"]


def here_or_there(word_list, letter, num_1, num_2):
    """
    Given a list, letter x, and two indecies, determines
    which index x occurs at most for each word in
    the list.

    O(n)

    @param: word_list = The list of words word_list will scan.
    @param: letter = the letter to check indecies for.
    @param: num_1 = the first index to check.
    @param: num_2 = the second index to check.
    @return: the index of the given two which x occurs most,
        if the two indecies have equal occurances of x
        -1 will be returned, if one of the given indecies
        is out of range for all words (word length: 7, index 7)
        (negative indecies as well) 2 is returned. If more than
        a single letter is entered, -3 is returned.
    """
    num_1_counter = 0
    num_2_counter = 0
    invalid_index = True
    invalid_letters = True

    if (num_1 >= 0) & (num_2 >= 0) & ((len(letter)) == 1):
        invalid_letters = False
        for x in (word_list):
            if (len(x) >= 5) & (num_1 < len(x)) & (num_2 < len(x)):
                invalid_index = False
                if x[num_1] == letter:
                    num_1_counter += 1

                if x[num_2] == letter:
                    num_2_counter += 1
    if invalid_letters:
        return -3
    elif invalid_index:
        return -2
    elif num_1_counter > num_2_counter:
        return num_1
    elif num_1_counter < num_2_counter:
        return num_2
    else:
        return -1

'''
Finds all the anagrams of a word in a text file
Precondition: word must be a valid word w/ alphanumeric characters only.

# @param word The word of interest that we will return all the possible words with
# @return An array of words that are anagrams of our word
# Runtime: O(nk) where k is the length of the word, and n is the length of the text file.
    Contains 1 nested loop which iterates over the length of the text file and the length
    of the inputted word, thus having O(nk) where n is the size of the text file and k
    is the length of the word inputted.

'''
def Anagram(word):
    f = open("words.txt", "r")
    
    words = f.read().splitlines()
    word_letters = {} # the dictionary / map containing all freq of letters in word
    arr_of_letters = [] # an array containing maps of all freq of letters in word
    arr_of_valid_words = [] # the valid words that will be returned 

    total_length = len(word)
    for letter in word: # adds up the frequency of each letter in the word
        word_letters[letter] = word_letters.get(letter, 0) + 1 
    
    for x in words:
        if(len(x) == total_length):
            letters_in_arr = {"original_word": x} # used to keep track of the actual word
            for letter in x: # adds up the frequency of each letter of each word in file
                letters_in_arr[letter] = letters_in_arr.get(letter,0) + 1
            arr_of_letters.append(letters_in_arr)
    
    
    for dictionary in arr_of_letters:
        valid_to_push = True
        for key in word_letters: 
            if(dictionary.get(key,0) != word_letters.get(key,0)):
                valid_to_push = False #checks to see if every frequency is the same
                break
        if(valid_to_push):
            arr_of_valid_words.append(dictionary["original_word"])

    return arr_of_valid_words

'''
Finds all the anagrams of a word in a text file
Precondition: word must be a valid word w/ alphanumeric characters only.

# @param word The word of interest that we will return all the possible words with
# @return An array of words that are anagrams of our word
# Runtime: O(nk) where k is the length of the word, and n is the length of the text file.
    Contains 1 nested loop which iterates over the length of the text file and the length
    of the inputted word, thus having O(nk) where n is the size of the text file and k
    is the length of the word inputted.

'''
def Anagrams_Minus_One(word):
    f = open("words.txt", "r")
    
    words = f.read().splitlines()
    #figure out how to split this instantly
    word_letters = {} # the dictionary / map containing all freq of letters in word
    arr_of_letters = [] # an array containing all dicts of freq of letters in word in txt
    arr_of_valid_words = [] # the valid words that will be returned by the function
    total_length = len(word) 
    for letter in word:
        word_letters[letter] = word_letters.get(letter, 0) + 1
    
    for x in words:
        if(len(x) == total_length - 1): # ensures that the word in file is valid
            letters_in_arr = {"original_word": x}
            for letter in x:
                letters_in_arr[letter] = letters_in_arr.get(letter,0) + 1
            arr_of_letters.append(letters_in_arr)
    
    
    for dictionary in arr_of_letters:
        difference = 0; 
        for key in word_letters:
            difference = difference + abs(dictionary.get(key,0) - word_letters.get(key,0))
        
        if(difference == 1): # tracks the difference of letters such that if it is off by 1 it is valid
            arr_of_valid_words.append(dictionary["original_word"])

    return arr_of_valid_words

def mostletters(search):
    wordlist = open("wordlist.txt", 'r')
    wordlist = wordlist.read().splitlines()
    listlen = len(wordlist) - 1
    for i in (range(listlen)):
        for i2 in(range(listlen)):
            letcount1 = 0
            letcount2 = 0
            wrd1 = wordlist[i2]
            wrd1list = list(wrd1)
            wrd2 = wordlist[i2 + 1]
            wrd2list = list(wrd2)
            for i3 in range(len(wrd1list)):
                if search == wrd1list[i3]:
                    letcount1 += 1
            for i3 in range(len(wrd2list)):
                if search == wrd2list[i3]:
                    letcount2 += 1
            if letcount1 > letcount2:
                temp = wrd2
                wordlist[i2 + 1] = wrd1
                wordlist[i2] = temp
            elif letcount1 == letcount2 and len(wrd1) < len(wrd2):
                temp = wrd2
                wordlist[i2 + 1] = wrd1
                wordlist[i2] = temp
            elif letcount1 == letcount2 and len(wrd1) == len(wrd2):
                if wrd1list[0] == search and wrd2list != search:
                    temp = wrd2
                    wordlist[i2 + 1] = wrd1
                    wordlist[i2] = temp
    return wordlist


def menu_phase(phase):
    
    for x in range(100):
        print("\n")
        
    print("𝐈𝐂𝐒𝟒𝐔𝟏'𝐬".center(53))
    
    for x in title:
        print(x.center(50))
    
    print("\n")

    if phase == 1:
        for x in f_button:
            print(x.center(53))
        print("Words".center(53))
        print("Credits".center(53))
        
    if phase == 2:
        print("Functions".center(53))
        for x in w_button:
            print(x.center(53))
        print("Credits".center(53))

    if phase == 3:
        print("Functions".center(53))
        print("Words".center(53))
        for x in c_button:
            print(x.center(53))

def print_function_selection(selection):
    for x in f_button:
        print(x.center(53))

    print("\n")
    
    for x in range(len(functions)):
        if x == selection - 1:
          print(("| " + functions[x] + " |").center(53))
        else:
          print(functions[x].center(53))

def function_menu():
    selection = 1
    moves = ["w", "s"]
    move = "s"
    if move in moves:
        while move != "\n":
          for x in range(100):
            print("\n")
          print_function_selection(selection)
          move = getkey.getkey()
          if move == "s" and selection < len(functions):
            selection += 1
          elif move == "w" and selection > 1:
            selection -= 1
    for x in range(100):
        print("\n")
    if selection == 1:
        ##Instert call for All vowels
        print("All Vowels")
    elif selection == 2:
        ##Most Letters
        word = input("Word: ")
        return mostletters(word)
    elif selection == 3:
        ##Instert call for Backwards
        print("Merica")
    elif selection == 4:
        ##Instert call for Odd/Even
        print("Merica")
    elif selection == 5:
        ##Instert call for Wordle Panic
        print("Merica")
    elif selection == 6:
        ##Instert call for Crossword Solver
        print("Merica")
    elif selection == 7:
        ##Instert call for Minus One
        print("Merica")
    elif selection == 8:
        ##Instert call for Plus One
        print("Merica")
    elif selection == 9:
        ##Instert call for Anagram
        word = input("Word: ")
        return Anagram(word)
    elif selection == 10:
        ##Instert call for Anagrams Minus One
        word = input("Word: ")
        return Anagram(word)
    elif selection == 11:
        letter = input("letter: ")
        num_1 = int(input("Index 1: "))
        num_2 = int(input("Index 2: "))
        common_index = here_or_there(words_list, letter, num_1, num_2)
        #print(letter + " appears most at index " + str(common_index))
        print(common_index)
        

def words():
    for x in range(100):
        print("\n")
    
    print("(m) return to menu")
    print("\n")
    
    for x in w_button:
        print(x.center(53))
    print("\n")
    for x in range(len(words_list)):

        for y in range(20):
            print(" ", end = "")

        print(str(x + 1) + ".  " + words_list[x])

    while True:
        exit = getkey.getkey()
        if exit == "m":
          break
    menu()

def credits():
    
    for x in range(100):
        print("\n")
    
    print("(m) return to menu")
    print("\n")
    
    for x in c_button:
        print(x.center(53))
    print("\n")

    print("𝐖𝐨𝐫𝐝 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠")
    print("\n")

    print("𝐂𝐥𝐢𝐞𝐧𝐭: " + "Monarch Park Collegiate")
    print("𝐕𝐞𝐫𝐬𝐢𝐨𝐧: " + version)
    print("𝐂𝐥𝐢𝐞𝐧𝐭 𝐏𝐨𝐢𝐧𝐭 𝐎𝐟 𝐂𝐨𝐧𝐭𝐚𝐜𝐭: " + "Mr. Jamieson")
    print("𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐌𝐚𝐧𝐚𝐠𝐞𝐫𝐬: " + "Olivia Chezzi, Aidan McFadden")
    print("")

    for g in range(55):
        print("_", end = "")
    print("\n")
    print("𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧".center(8), end = "")
    print("𝐀𝐮𝐭𝐡𝐨𝐫𝐬".center(32))
    for g in range(55):
        print("_", end = "")
    
    print("\n")
    
    for x in range(len(functions)):
        print(functions[x], end = "")
        
        for y in range(20 - (len(functions[x]))):
            print(" ", end = "")
            
        print(authors[x], "\n")
    
    while True:
        exit = getkey.getkey()
        if exit == "m":
          break
    menu()

def menu():
    option = 1
    moves = ["w", "s"]
    move = "s"
    if move in moves:
        while move != "\n":
            menu_phase(option)
            move = getkey.getkey()
            if move == "s" and option < 3:
                 option += 1
            elif move == "w" and option > 1:
                option -= 1
    if option == 1:
        function_menu()
    elif option == 2:
        words()
    elif option == 3:
        credits()

menu()