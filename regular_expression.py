import re

digit = re.compile("\d")  # Which represent all digits [0-9]
print(digit.findall("Hello! It's 10:30 now."))

mul_digit = re.compile("\d+")   # Which represent pair of digits
print(mul_digit.findall("Hello! It's 10:30 now."))

alpha_num = re.compile("\w+")   # Which represent pair of alphanumeric characters
print(alpha_num.findall("Hello! It's 10:30 now."))

char_pair = re.compile("ab*")   # Which represent pair of ab, abb, abbb...
print(char_pair.findall("abaabbbbbabababbbabbb"))

print(re.sub('a', '0', "Hello! How are you!"))

print(re.search('H', "Hello! How do you do?"))
