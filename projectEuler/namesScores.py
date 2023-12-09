def calculate_name_scores():
    # Read the contents of names.txt and extract the names
    with open('C:/Users/User/PycharmProjects/projectEuler/names.txt', 'r') as file:
        names = file.read().replace('"', '').split(',')

    # Sort the names into alphabetical order
    names.sort()

    # Function to calculate the alphabetical value of a name
    def alphabetical_value(name):
        return sum(ord(char) - ord('A') + 1 for char in name)

    # Calculate the total name scores
    total_score = 0
    for idx, name in enumerate(names, start=1):
        score = alphabetical_value(name) * idx
        total_score += score

    return total_score

# Calculate the total of all name scores
result = calculate_name_scores()
print(f"The total of all the name scores in the file is: {result}")
