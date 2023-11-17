# Write a code to encode a string from 'aaabbcc' to 'a3b2c2'
# code 1
# def encode(s):
#     encoded = ""
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count += 1
#             i += 1
#         encoded += s[i] + str(count)
#         i += 1
#     return encoded

# print(encode("aaabbcc"))

# code 2
# def encoded_string(input_string):
#     encoded_string = ""
#     count = 1
#     for i in range(len(input_string)-1):
#         if input_string[i] == input_string[i+1]:
#             count += 1
#         else:
#             encoded_string += input_string[i] + str(count)
#             count = 1
#     encoded_string += input_string[-1] + str(count)
#     return encoded_string

# print(encoded_string("aaabbcc"))

def encode_string(input_string):
    encode_string = ""
    character_counts = {}

    for character in input_string:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    for character, count in character_counts.items():
        encode_string += character + str(count)

    return encode_string


print(encode_string("aaabbcc"))


