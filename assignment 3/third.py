# 3) Remove all duplicate words and recalculate the number of words

file = open("zen.txt", "r")
zen_text = file.read()
file.close()



def count_unique(text):
    unique_words = set()
    single_word = ""
    
    for char in text:
        if char.isalpha() or char == "'":
            single_word += char.lower()
        elif single_word: 
            unique_words.add(single_word) 
            single_word = ""
    
    # Add the last word if it exists
    if single_word:
        unique_words.add(single_word)
    
    return len(unique_words) 


print("Total unique English words:", count_unique(zen_text))
