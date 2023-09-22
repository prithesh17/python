string = input("Enter the sentence: ")
digit_count, uppercase_count, lowercase_count=0,0,0
list_of_words=string.split()
word_count=len(list_of_words)
for char in string :
    if char.isdigit():
       digit_count+=1
    elif char.isupper():
        uppercase_count+=1
    elif char.islower():
        lowercase_count+=1
print("Number of words: ",word_count)
print("Number of digits: ",digit_count)
print("Number of uppercase letters: ",uppercase_count)
print("Number of lowercase letters: ",lowercase_count)
