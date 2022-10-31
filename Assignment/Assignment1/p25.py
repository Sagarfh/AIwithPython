#Program to Check Whether a String is Palindrome or Not
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# main function
s = input("Enter the string to check : ")
ans = isPalindrome(s)

if (ans):
    print("Given string",s," is a palendrome")
else:
    print("Given string",s," is not a palendrome")