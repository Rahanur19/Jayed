# 1) Count all English words

file = open("zen.txt", "r")
zen_text = file.read()
file.close()


def count_words(text):
    count = 0
    single_word = ""
    for char in text:
        # print(char)
        if char.isalpha() or char == "'":
            single_word += char.lower()  
        elif single_word:
            count += 1  
            single_word = ""  
    
    #if there's a word left at the end of the text
    if single_word:
        count += 1    
    return count

print("Total English words:", count_words(zen_text))
