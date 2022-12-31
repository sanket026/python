string_1 = "apple, pear"
string_2 = "orange, "

beginning_substring = string_1[:7]
ending_substring = string_1[7:]

inserted_string = beginning_substring + string_2 + ending_substring

print(inserted_string)