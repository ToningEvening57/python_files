def ispalindrome(word):
    if len(word) ==1:
        return True

    if len(word) ==2:
        return word[0] == word[1]

    if word[0] == word[-1]:
        return ispalidrome(word[1:-1])


    return False
    

palindrome = ['a', 'aa']


for word in palindrome:
    print(f"{word:12}")


print('Welcome!\nStart Program: [Y|N}')
input('_')
