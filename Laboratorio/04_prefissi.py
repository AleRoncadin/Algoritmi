from __future__ import print_function

try: input = raw_input
except NameError: pass

s = input()
for i in range(len(s)):
	print(s[0:len(s)-i])