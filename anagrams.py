# Finds all the anagrams of a word in a text file
# @param word The word of interest that we will return all the possible words with
# @return An array of words that are anagrams of our word

#Precondition: word must be a valid string w/ alphanumeric characters only.
def Anagram(word):
    f = open("words.txt", "r")
    
    words = f.read().splitlines()
    #figure out how to split this instantly
    word_letters = {}
    arr_of_letters = []
    arr_of_valid_words = []
    total_length = len(word)
    for letter in word:
        word_letters[letter] = word_letters.get(letter, 0) + 1
    
    for x in words:
        if(len(x) == total_length):
            letters_in_arr = {"original_word": x}
            for letter in x:
                letters_in_arr[letter] = letters_in_arr.get(letter,0) + 1
            arr_of_letters.append(letters_in_arr)
    
    
    for dictionary in arr_of_letters:
        valid_to_push = True
        for key in word_letters:
            if(dictionary.get(key,0) != word_letters.get(key,0)):
                valid_to_push = False
                break
        if(valid_to_push):
            arr_of_valid_words.append(dictionary["original_word"])

    return arr_of_valid_words

def Anagrams_Minus_One(word):
    f = open("words.txt", "r")
    
    words = f.read().splitlines()
    #figure out how to split this instantly
    word_letters = {}
    arr_of_letters = []
    arr_of_valid_words = []
    total_length = len(word)
    for letter in word:
        word_letters[letter] = word_letters.get(letter, 0) + 1
    
    for x in words:
        if(len(x) == total_length - 1):
            letters_in_arr = {"original_word": x}
            for letter in x:
                letters_in_arr[letter] = letters_in_arr.get(letter,0) + 1
            arr_of_letters.append(letters_in_arr)
    
    
    for dictionary in arr_of_letters:
        print(dictionary)
        print("\n")
        difference = 0; 
        for key in word_letters:
            difference = difference + abs(dictionary.get(key,0) - word_letters.get(key,0))
        
        if(difference == 1):
            arr_of_valid_words.append(dictionary["original_word"])

    return arr_of_valid_words

print(Anagrams_Minus_One("hello"))