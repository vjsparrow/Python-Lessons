class Solution:
    def romanToInt(self, s: str) -> int:
        
# Define the Roman-Int value pairs
        roman_to_int = {
                        'I' : 1, 
                        'V': 5, 
                        'X': 10, 
                        'L': 50, 
                        'C': 100, 
                        'D': 500, 
                        'M': 1000
                        }

# Create a variable int_val to store the corresponding int values as we read the string.
        int_val = 0
# If s is one character, then convert to int of the value of that character
        if len(s) == 1:
            int_val = roman_to_int[s[0]]
        else:
            i = 0
# Run through the length of the string and return the final value of int_val.
            while i < (len(s)):
                try:
# If s[i + 1] < s [i], add the int value of s[i] to the int_val.
                    if roman_to_int[s[i + 1]] <= roman_to_int[s[i]]:
                        int_val += roman_to_int[s[i]]
                        i += 1
# If s[i + 1] > s[i], add the int value of s[i + 1] - s[i] to int_val.
                    elif roman_to_int[s[i + 1]] > roman_to_int[s[i]]:
                        int_val += (roman_to_int[s[i + 1]] - roman_to_int[s[i]])
                        i += 2
                except IndexError:
                    int_val += roman_to_int[s[i]]
                    break

        return(int_val)
