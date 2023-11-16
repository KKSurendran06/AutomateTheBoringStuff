# 1
're.compile()'

# 2
raw string allow us to create patterns containing backslashes without escaping them

# 3
search() method returns the matched patterns from the Regex object

# 4
* print(Match.group())

# 5
* group(0) - ddd-ddd-dddd
* group(1) - ddd
* group(2) - ddd-dddd

# 6
* \( or \) - to escape parentheses

* \. - to escape period

# 7
if the regex expression is grouped using parentheses, it returns tuples or just as a list of string

# 8
it signifies or 

# 9 
it signifies zero or one of the preceding group also for non-greedy matching

# 10
* `+` - signifies one or more of the preceding group

* `*` - signifies zero or more of the preceding group

# 11
* {3} - 3 chars will be identified

* {3, 5} - 3 or 4 or 5 chars will be identified

# 12
* \d - includes digits

* \w - includes words

* \s - includes new line, tab, space

# 13
* \D - includes everything other than digits 

* \W - includes everything other than words

* \S - includes everything other than new line, tab, space

# 14 
* `.*`  - greedy  

* `.*?` - non-greedy 

# 15
[0-9a-z]

# 16
re.IGNORECASE

# 17
.(wildcard character) matches anything except a newline and if re.DOTALL is passed as second argument then it includes all new line character

# 18
'X drummers, X pipers, five rings, X hens'

# 19
it would allow us commenting inside the regex object making it more readable

# 20
re.compile(r'^\d{1,3}(,\d{3})*$')

# 21
re.compile(r'[A-Z](\w+) (Watanabe)')

# 22
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)(\.)', re.I)


