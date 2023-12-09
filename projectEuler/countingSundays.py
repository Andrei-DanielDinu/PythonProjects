import datetime

def count_sundays_on_first_of_month():
    # Initialize count to track Sundays on the first of the month
    sunday_count = 0

    # Iterate through each month and year in the twentieth century
    for year in range(1901, 2001):
        for month in range(1, 13):  # Month ranges from 1 to 12
            # Create a datetime object for the first day of each month
            first_day_of_month = datetime.datetime(year, month, 1)

            # Check if the first day of the month is a Sunday (weekday number 6)
            if first_day_of_month.weekday() == 6:  # 6 represents Sunday
                sunday_count += 1  # Increment count for Sundays on the first of the month

    return sunday_count

# Calculate the number of Sundays falling on the first of the month
result = count_sundays_on_first_of_month()
print(f"The number of Sundays falling on the first of the month during the twentieth century is: {result}")
