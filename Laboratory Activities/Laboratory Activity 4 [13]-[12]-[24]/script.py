from Capybara import Capybara

capybaras = [
    Capybara("Elaine", "M", 3),
    Capybara("Melens", "F", 4),
    Capybara("Max", "M", 2),
]

test_case = int(input("Enter test case number (1-3): "))
if 1 <= test_case <= len(capybaras):
    print(capybaras[test_case - 1])
else:
    print("Invalid test case number.")
