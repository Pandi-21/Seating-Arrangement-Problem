# Problem:
# Given a string consisting of letters and digits, separate and sort the letters and digits
# individually and then concatenate them with letters first followed by digits.

# solution:
# - Iterate through the string and separate letters and digits into two lists.
# - Sort both the lists.
# - Concatenate the sorted letters and digits and print the result.

def separate_sort(input_str):
    letters = sorted([str for str in input_str if str.isalpha()])
    digits = sorted([str for str in input_str if str.isdigit()])
    output = ''.join(letters) + ''.join(digits)
    print(output)
 
input_str =  "B4A1D3"
separate_sort(input_str)
