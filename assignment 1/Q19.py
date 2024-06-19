import string
 

test_str = "Gfg, is best : for ! Geeks ;"
print("The original string is : " + test_str)
for punctuation in string.punctuation:
    test_str = test_str.replace(punctuation, '')
 
print("The string after punctuation filter : " + test_str)