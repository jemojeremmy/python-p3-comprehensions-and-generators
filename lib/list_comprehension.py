# lib/list_comprehension.py

def return_evens(num_list):
    # Using list comprehension to filter even numbers
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    # Using list comprehension to add exclamation marks to each sentence
    return [sentence + "!" for sentence in sentence_list]
