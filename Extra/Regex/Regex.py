# Regex is majorly used for Pattern Matching
# Regex Practice - https://regexr.com/
# https://youtu.be/rhzKDrUiJVk
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#:~:text=Regular%20expressions%20are%20patterns%20used,split()%20methods%20of%20String%20.
# https://www.hackerrank.com/domains/regex?filters%5Bdifficulty%5D%5B%5D=easy
# + ? * . \w \s \W \S \w{4} \w{4,} \w{4,5}
# [fc] [a-z]
# () | ^ $
# Look Behind: (?<=). (?<!).
# Look Ahead: .(?=) .(?!)
# \d ?<>
# Non Capturing Group: ?:()
# Pattern to match all below numbers: (?:(\+1)[- ])?\(?(?<areacode>\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})
# 1234567890
# 123-456-7890
# 123 456 7890
# (123) 456 7890
# +1 123 456 7890

import re

# Only upper case letters
pattern = re.compile("^[A-Z]+$")

"""
The carrot sign (^) defines that the first element should be upper case.
The Dollar sign ($) defines that the end of the String should be upper case.
[A-Z] represents the String should have only capital A to Z.
+ represents that there must be atleast one but can be more than 1 A to Z characters

The ^ and $ are making the pattern eligible for the whole string.

So, the whole string should have uppercase string.
"""

print(pattern.search('Hello World')) # None
print(pattern.match('Hello World')) # None
print(pattern.search("HELLO WORLD")) # None
print(pattern.match("HELLO WORLD")) # None
print(pattern.search("HELLOWORLD")) # <re.Match object; span=(0, 10), match='HELLOWORLD'>
print(pattern.match("HELLOWORLD")) # <re.Match object; span=(0, 10), match='HELLOWORLD'>

"""
search vs match:
match looks into the starting. Basically it returns that much part of the string that matches the pattern from the start of the string.
If there is no match at the start then it returns None, else returns the string till the point the pattern is matching.

search looks into the whole string and returns the part of the string that matched the pattern.
"""

pattern = re.compile("[a-z]+")
print(pattern.search("Hello World")) # <re.Match object; span=(1, 5), match='ello'>
print(pattern.match("Hello World")) # None
print(pattern.match("hello world")) # <re.Match object; span=(0, 5), match='hello'>
print(pattern.match("helloworld")) # <re.Match object; span=(0, 10), match='helloworld'>