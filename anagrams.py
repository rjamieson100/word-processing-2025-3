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
