def number_to_words(n):
    # Define word representations for numbers up to 19
    num_dict = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen'
    }
    # Define word representations for tens
    tens_dict = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    if n == 1000:
        return 'onethousand'

    if n >= 100:
        hundreds = num_dict[n // 100] + 'hundred'
        if n % 100 != 0:
            hundreds += 'and'
        return hundreds + number_to_words(n % 100)

    if n >= 20:
        return tens_dict[n // 10] + num_dict[n % 10]

    return num_dict[n]

def count_letters_in_numbers(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        word_representation = number_to_words(i)
        total_letters += len(word_representation)
    return total_letters

result = count_letters_in_numbers(1000)
print(f"The total number of letters used from 1 to 1000 is: {result}")
