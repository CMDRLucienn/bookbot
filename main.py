# Imports
from collections import Counter

# Parameters
book_path = "./books/"
book = "frankenstein.txt"

def count_words(text_string):
    count = 0
    words = text_string.split()
    for word in words:
        count += 1

    return count

def count_characters(text_string):
    character_list = list(text_string.lower())
    character_count = dict(Counter(character_list))
    character_dict = {k: v for k, v in sorted(character_count.items(), reverse=True, key=lambda x: x[1])}
    for char in list(character_dict):
        if not char.isalpha():
            del character_dict[char]

    return character_dict

def construct_report(word_count, char_dict):
    report = f"--- Begin report of {book_path}{book} ---\n"
    report += f"{word_count} words found in the document\n\n"

    for char in char_dict:
        report += f"The '{char}' character was found {char_dict[char]} times\n"

    report += f"--- End report ---"
    
    return report

### MAIN
def main():
    with open(book_path + book) as f:
        file_contents = f.read()
 
    print(construct_report(count_words(file_contents), count_characters(file_contents)))

### CALL MAIN
main()