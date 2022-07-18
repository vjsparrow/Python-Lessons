## Problem - Rotated Lists
# Assuming all elements are unique
# Assuming original list is sorted
# State the problem clearly.
# *** Problem solving strategy ***
# Identify the input & output formats.
# Come up with some example inputs & outputs. Try to cover all edge cases.
# Come up with a correct solution for the problem. State it in plain English.
# Implement the solution and test it using example inputs. Fix bugs, if any.
# Analyze the algorithm's complexity and identify inefficiencies, if any.
# Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
# ********************************** #

# Input = a list of numbers. Call it rotated_list in the code.
# Output = an integer. Number of times it takes to rotate the original list.
# Call it no_of_rotations.
# Example input cases:
    # 1. rotated_list was not rotated and is the same as original list.
    # 2. rotated_list rotated n times where 0 < n < len(original_list)
    # 3. Original list was empty and so is the rotated_list.
    # 4. rotated_list rotated n times where n > len(original_list)
# Findings:
    # 1. rotated_list sorted exactly len(original_list) times will just get back to
    #     original_list and then we start over.
    # 2.
# Correct Solution:
# 1. Accept input of a rotated list.
# 2. Check if the list is empty. If so, return output for test case 3.
# 3. Check if the list is sorted. If so, return 0.
# 4. Find the smallest item in the list and return it's position.
# 5. Since we only need minimum number of rotations, we can simpy calculate
#     the offset of the smallest item from 0.

test_cases = {
                {"input":[5, 6, 7, 1, 2, 3, 4],
                "output":'3'
                }
                {"input":[],
                "output":'Original list was empty'
                }
                {"input":[10, 20, 30],
                "output": '0'}
                {"input":[11,2,3,4],
                "output": '1'}
            }


def rotated_list(input_list):

    try:
        smallest = min(input_list)
        smallest_pos = input_list.index(smallest)

        if smallest_pos == 0:
            print("0")
        else:
            return print(smallest_pos)
    except ValueError:
        print("List was empty!")


rotated_list([45, 67, 89, 90, 5, 11, 15])
