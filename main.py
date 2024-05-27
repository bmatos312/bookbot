#!/usr/bin/env python3

def main():
    
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
    
    # Split the contents into words
    words = file_contents.split()
    
    # Get the word count
    word_count = len(words)
    
    # Get the character counts
    char_counts = count_characters(file_contents)
    
    # Generate the report
    report = generate_report(word_count, char_counts)
    
    # Print the report
    print(report)

def count_characters(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Create a dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def generate_report(word_count, char_counts):
    report = []
    report.append(f"Total number of words: {word_count}")
    report.append("Character counts:")
    
    for char, count in sorted(char_counts.items()):
        report.append(f"'{char}': {count}")
    
    return "\n".join(report)

if __name__ == "__main__":
    main()

