# Function to detect all occurrences of a substring (substr or pattern) of length `m`
# in a given string (text) of length `n`
def detect(str, substr):

	n = len(string)
	m = len(substr)

	# base case 1: substr is empty, an empty substr elvaluates to False
	if not substr:
		print('The substr occurs with shift 0')
		return

	# base case 2: str is None, or str length is less than that of substr
	if not string or len(substr) > len(string):
		print('substr not found')
		return

	i = 0
	while i <= n - m:
		for j in range(m):
			if string[i + j] is not substr[j]:
				break
			if j == m - 1:
				print('Substring occurs with shift', i)
				i=i+j # save iterations over the length of complete detected substr
		i = i + 1


if __name__ == '__main__':

	string = 'ABCABAABCABAC'
	substr = 'CAB'

	detect(string, substr)
