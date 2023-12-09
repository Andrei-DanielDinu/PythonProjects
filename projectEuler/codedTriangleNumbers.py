def is_triangular(num):
    # Check if a number is a triangular number
    n = int((2 * num) ** 0.5)
    return n * (n + 1) == 2 * num

def word_value(word):
    # Calculate the word value for a given word
    return sum(ord(char) - ord('A') + 1 for char in word)

def count_triangle_words():
    # Read words from the file
    with open('words.txt', 'r') as file:
        words = file.read().replace('"', '').split(',')

    triangle_words = 0
    for word in words:
        value = word_value(word)
        if is_triangular(value):
            triangle_words += 1

    return triangle_words

result = count_triangle_words()
print(f"The number of triangle words is: {result}")
