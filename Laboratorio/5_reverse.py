from __future__ import print_function

try: input = raw_input
except NameError: pass

s = input()

t = ""
for i in range(0, len(s)):
    t = s[i] + t

print(t)

print(s[::-1])

print(s[len(s)-1:0])
