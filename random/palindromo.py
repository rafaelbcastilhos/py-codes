'''This function checks the string for palindrome'''
def palindrome(string):
    revString = string[::-1]
    if string == revString:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

if __name__ == '__main__':
    userInput = str(input('Enter a string to check for Palindrome: '))
    palindrome(userInput)