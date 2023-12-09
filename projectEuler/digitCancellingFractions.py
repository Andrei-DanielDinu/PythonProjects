from fractions import Fraction

def curious_fractions():
    fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            num_digits = str(numerator)
            den_digits = str(denominator)
            common_digit = set(num_digits) & set(den_digits)
            if len(common_digit) == 1 and '0' not in common_digit:
                common_digit = list(common_digit)[0]
                num_digits = num_digits.replace(common_digit, '', 1)
                den_digits = den_digits.replace(common_digit, '', 1)
                if int(den_digits) != 0 and Fraction(numerator, denominator) == Fraction(int(num_digits), int(den_digits)):
                    fractions.append(Fraction(numerator, denominator))

    return fractions

fractions_list = curious_fractions()
product = Fraction(1, 1)
for fraction in fractions_list:
    product *= fraction

denominator_value = product.denominator
print("The value of the denominator of the product of these fractions is:", denominator_value)
