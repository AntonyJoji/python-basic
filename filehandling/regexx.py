import re

##     . : to match any charaters
##     ^ : start
##     $ : end
##     * : 0 or more
##     ? : 0 or 1
##     + :1 or more
##    {n}: exactly n repetations
##   {n,}:n or more
##     []: char set [a-z],[0-9]
##    [^]:not these char
##    \d :digit(0-9)
##    \D : non digits
##    \w :word char(A-Z,a-z,0-9,_)
##    \W :non word char
##    \s:space
##    \S:non space
##    ():group for capturing
##    \b:word boundary
##    \B:non word boundary

# text_to_search = '''
#     abcdefghijklmnopqrstuvwxyz
#     ABCDEFGHIJKLMNOPQRSTUVWXYZ
#     1234567890
#     Ha HaHa
#     MetaCharacters (need to be escaped):
#     . ^ $ * + ? { } [ ] \ / ( )
#     coreyms.com
#     321-555-4321
#     123.555.1234
#     123*555*1234
#     900-555-1234
#     Mr. Schafer
#     Mr Smith
#     ms Davis
#     Mrs. Robinson
#     Mr. T
# '''
# print (r"\new")
# print (r"\tab")


# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


 ## to save data in a variable
# pattern = re.compile(r'.')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)

# res = text_to_search[0:3]
# print(res)


### for finding "."

# pattern = re.compile(r'\.')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)

# res = text_to_search[0:3]
# print(res)


# pattern = re.compile(r'ms.com')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\d')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\D')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'/w')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)



# pattern = re.compile(r'\s')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)
# pattern = re.compile(r'\bHs')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\BHs')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)
   

# sentence = 'start a sentence and then bring it to an end'
# pattern = re.compile(r'^Start')
# matches = pattern.finditer(sentence)
# print (matches)
# for match in matches:
#     print(match)

# sentence = 'start a sentence and then bring it to an end'
# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
# print (matches)
# for match in matches:
#     print(match)



text_to_search = '''
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
    Ha HaHa
    MetaCharacters (need to be escaped):
    . ^ $ * + ? { } [ ] \ / ( )
    coreyms.com
    321--555--4321
    123.555.1234
    123*555*1234
    900--555--1234
    500--555--1234
    Mr. Schafer
    Mr Smith
    ms Davis
    Mrs. Robinson
    Mr. T
    cat
    mat
    pat
    bat

'''

# pattern = re.compile(r'\d\d\d\W\d\d\d\W\d\d\d\d')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\d{3}\W\d{3}\W\d{4} ')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{3}.\d{3}.d{4} ')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\d{3}..\d{3}..\d{4}')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\d{3}--\d{3}--\d{4}')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)



# pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)


# pattern = re.compile(r'\d{3}[-]+\d{3}[-]+\d{4}')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)

# pattern = re.compile(r'[59]00[-]+\d{3}[-]+\d{4}')
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)

# pattern = re.compile(r'[^b]at') ## ends with 'at'
# matches = pattern.finditer(text_to_search)
# print (matches)
# for match in matches:
#     print(match)

    
