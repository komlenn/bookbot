from string import ascii_lowercase as asc

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = dict_to_list(chars_dict)

    print(f"--- Begin report of {book_path}\n {num_words} words found in document\n" )

    for i,y in sorted_list:
        print(f"The {i} character was found {y} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
#def get_chars_dict(text):
    chars = {}
    for c in text:
        lowerd = c.lower()
        if lowerd in chars:
            chars[lowerd] += 1
        else:
            chars[lowerd] = 1
    return chars

def get_chars_dict(text):
    chars = {}
    for i in asc:
        counter = 0
        for char in text:
            if i == char.lower():
                counter += 1 
            chars[i] = counter
    return chars

def dict_to_list(chars_dict):
    def takeSecond(elem):
        return elem[1]
    
    new_list = []
    for key, val in chars_dict.items():
        new_list.append([key, val])
    new_list.sort(key=takeSecond, reverse=True)
    return new_list







    
main()