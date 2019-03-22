# Write a Python program to get a single string
# from two given strings, separated by a space
# and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


def get_single_string(str1, str2):
    first_two = str1[0:2]
    second_two = str2[0:2]
    return second_two + str1[2:] + " " + first_two + str2[2:]
print(get_single_string('abc', 'xyz'))
