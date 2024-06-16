def lengthOfLongestSubstring(s: str) -> int:
	window = ''
	longest = ''
	i = 0
	j = 0
	found = False

	while i < len(s) and not found:
		j = i
		while j < len(s) and s[j] not in window:
			window += s[j]
			j += 1
		if len(window) > len(longest):
			longest = window
		if len(longest) >= len(s) - i:
			found = True
		window = ''
		i += 1
	return len(longest)

def main():
	s = 'pwwkew'
	print(lengthOfLongestSubstring(s=s))

if __name__ == '__main__':
	main()
