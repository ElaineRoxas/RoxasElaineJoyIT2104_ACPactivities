def find_vowels(string):
    vowels = "aeiouAEIOU"
    result = [char for char in string if char in vowels]
    return result

input_string = input("Enter a string: ")

vowel_list = find_vowels(input_string)
print(vowel_list)
