## write a function to return most repeted charater in a string
# val ="success"

# def most_repeated_char(s):
#     max_count = 0
#     result = ""

#     for ch in s:
#         count = s.count(ch)
#         if count > max_count:
#             max_count = count
#             result = ch

#     return result


# val = "success"
# print(most_repeated_char(val))
### or

def most_repeated_char(s):
    char_count = {}
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    max_count = 0
    result = ""
    for ch, count in char_count.items():
        if count > max_count:
            max_count = count
            result = ch

    return result

val = "success"
print(most_repeated_char(val))                   