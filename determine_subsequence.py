# Function to determine if a string is a subsequence of another string

def subsequence(A, B):
	# base case: an empty string is a subsequence of any string
	if not B:
		return True

	# index for the next character of the second string
	j = 0

	# iterate over each character of the first string
	for i in A:
		# if the current character matches the next character of the second string
		if i == B[j]:
			# increment the index and return true if end of second string is reached
			j = j + 1
			if j == len(B):
				print('Subsequence found')
				return 

	# we reach here only if second string is not a subsequence of first string
	print('Not a subsequence')
	return 


if __name__ == '__main__':
	A = 'abcde'
	B = 'abe'
	subsequence(A, B)
