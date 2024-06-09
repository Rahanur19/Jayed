# 2) Get the word with the highest frequency of occurrence

file = open("zen.txt", "r")
zen_text = file.read()
file.close()


def count_word_numbers(text):
    word_num_dic = {}  
    single_word = ""

    for char in text:
        if char.isalpha() or char == "'":
            single_word += char.lower()
        elif single_word:
            word_num_dic[single_word] = word_num_dic.get(single_word, 0) + 1
            single_word = ""
    
    if single_word:
        word_num_dic[single_word] = word_num_dic.get(single_word, 0) + 1
    
    return word_num_dic

number_of_each_word = count_word_numbers(zen_text)

highest_frequent = max(number_of_each_word, key=number_of_each_word.get)
highest_frequency = number_of_each_word[highest_frequent]

print(f"The highest frequent word is : '{highest_frequent}' and it repeats {highest_frequency} times")
