# level 1
def count_words_and_characters(text):
    words = text.split()

    text = text.lower()
    character_counts = {}

    for char in text:
        if char.isalpha():
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1

    return words, character_counts

try:
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        result = count_words_and_characters(file_contents)

        words = result[0]
        character_counts = result[1]

        word_count = len(words)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        for char in sorted(character_counts.keys()):
            count = character_counts[char]
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")

except FileNotFoundError:
    print("The file 'frankenstein.txt' was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {str(e)}")
