# Implement Knuth-Morris-Pratt algorithm to match a pattern 'p' in a given text 't'
# This is Algo-Expert's implementation


def knuth_morris_pratt(t, p):
	automata = create_automata(p)
	return (does_match(t, p, automata))


# Create the automata
def create_automata(p):
	i = 1
	j = 0
	automata = [-1 for i in p]
	while i < len(p):
		if p[i] == p[j]:
			automata[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = automata[j - 1] + 1
		else:
			i += 1
	return (automata)


# Search for the pattern in the text
def does_match(t, p , automata):
	i = 0
	j = 0
	while i + len(p) - j <= len(t):
		if t[i] == p[j]:
			if j == len(p) - 1:
				return True
			else:
				i += 1
				j += 1
		elif j > 0:
			j = automata[j - 1] + 1
		else:
			i += 1
	return False


# Tested using the below strings
# t = 'haystackwithstickboy'
# p = 'stick'
# print(knuth_morris_pratt(t, p))
