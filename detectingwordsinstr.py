import re

def extract_words(input_string):
    # Use a regular expression to split the string based on key representations
    individual_words = re.split(r'(Key\.\w+)', input_string)

    # Remove empty strings from the list
    individual_words = [word.replace(" ",'') for word in individual_words]


    return individual_words

# Example usage:
input_string = "h e l l o Key.space i Key.space h a v e Key.space a Key.space h u f e Key.backspace Key.backspace g e Key.space y e l l o Key.space b o o k . Key.backspace Key.esc"
result = extract_words(input_string)
print(result)
