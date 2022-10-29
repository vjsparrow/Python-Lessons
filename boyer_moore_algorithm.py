# Implement the Boyer-Moore Algorithm to match a pattern within a text


def boyer_moore(t, p):
	# Initialize an empty dictionary and store last positions of each character in the pattern
	last_position_in_p = {}
	for i in range(len(p)):
		last_position_in_p[p[i]] = i
	# Initialize a list to store indices of matched positions of the pattern in the text
	matched_positions = []
	# Run throught the length of the text and look for matches
	i = 0
	while i <= (len(t) - len(p)):
		j = len(p) -1
		matched = True
		while j >= 0 and matched:
			if t[i + j] != p[j]:
				matched = False
			j -= 1
		# If a match is found, append the match position to the list of matched positions
		if matched:
			matched_positions.append(i)
			i += 1
		# If there's a mismatch:
		else:
			# Restore the previously decremented value of j
			j += 1
			# If the mismatched character is in the pattern:
			if t[i + j] in last_position_in_p.keys():
				# If the mismatched character is before j, shift the scan by j-last[t[j]] positions
				# If the mismatched character appears after j, just shift the scan by 1 to the right
				i = i + max(j - last_position_in_p[t[i + j]], 1)
			# If the mismatched character is not in the pattern, shift the scan by 1 to the right
			else:
				i = i + j + 1
	# Return the list of matched positions
	return (matched_positions)

# Used the below string to test
# t = 'haystackwithstick'
# p = 'stick'
# print(boyer_moore(t, p))
