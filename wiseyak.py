""" Hi this was the question ask in the data engineer role in wiseyak. the problem is we need to find the combination of words using the phone number 
 and print the words if it is available in the sample dictionary provided by them.
 for example if a user select 228 then 2 corresponds to letter "a,b,c"  and 8 corresponds to "t,u,v"
 then the output must be  act, bat and cat
 similarly
 input 7625387  will output pockets rockets sockets
 
 """

import pandas as pd
df = pd.read_csv(r'C:\Users\user\Desktop\sample_dictionary.csv', header = None)

words = df.values.tolist()

def generate_combinations(digit):
    digit_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    return digit_to_letters.get(digit, [])

def generate_phone_number_combinations(phone_number):
    if not phone_number.isdigit():
        return "Invalid input: Enter digits only"
    
    combinations = ['']
    for digit in phone_number:
        if digit == '0' or digit == '1':
            return "Invalid input: 0 and 1 have no corresponding letters"
        
        new_combinations = []
        for combination in combinations:
            letters = generate_combinations(digit)
            new_combinations.extend([combination + letter for letter in letters])
        combinations = new_combinations
    
    return combinations

# Example usage
phone_number = input("Enter a phone number (digits only): ")
combinations = generate_phone_number_combinations(phone_number)

dict_word = [dict[0] for dict in words]
output_word = [element for element in combinations if element in dict_word]

print("The available words are:", output_word)
