def roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman.upper()):
        value = roman_values.get(char, 0)
        if value == 0:
            return "Invalid Roman numeral"
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

roman = input("Enter a Roman numeral: ")
print(f"Integer value of: {roman_to_integer(roman)}")
