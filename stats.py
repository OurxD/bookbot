def get_words_count(book_content):
    word_list = book_content.split()
    return len(word_list)

def get_char_count(book_content):
    char_dict = {}

    for char in book_content:
        lowercased_char = char.lower()
        if lowercased_char in char_dict:
            char_dict[lowercased_char] += 1
        else:
            char_dict[lowercased_char] = 1

    return char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def get_sorted_char_list(char_dict):
    char_list = []

    for char in char_dict:
        if char.isalpha():
            char_list.append({
                "char": char,
                "num": char_dict[char]
            })

    char_list.sort(reverse=True, key=sort_on)

    return char_list
