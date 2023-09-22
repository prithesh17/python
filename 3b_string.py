str1 = input("Enter the first string:\n")
str2 = input("Enter the second string:\n")

if len(str2) < len(str1):
    short_str_len = len(str2)
    long_str_len = len(str1)
else:
    short_str_len = len(str1)
    long_str_len = len(str2)

match_count = 0
for i in range(short_str_len):
    if str1[i] == str2[i]:
        match_count += 1

similarity = match_count / long_str_len
print("Similarity between the two strings:",similarity)

